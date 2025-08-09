"""CSV export functionality for RedLite runs."""

import csv
import json
import os
from typing import List, Optional, Tuple
from ._util import redlite_data_dir, read_runs, read_data, read_meta
from ._core import Run


def get_latest_run() -> Optional[str]:
    """
    Get the name of the most recently completed run.
    
    Returns:
        Name of the latest run, or None if no runs found.
    """
    base_dir = redlite_data_dir()
    runs = list(read_runs(base_dir))
    
    if not runs:
        return None
    
    # Sort by completion time (most recent first)
    runs.sort(key=lambda x: x["completed"], reverse=True)
    return runs[0]["run"]


def export_latest_run_to_csv(
    output_file: str,
    *,
    include_messages: bool = True,
    flatten_messages: bool = False
) -> bool:
    """
    Export the latest run to CSV format.
    
    Args:
        output_file: Path to the output CSV file
        include_messages: Whether to include the conversation messages in the export
        flatten_messages: If True, converts messages to a single string. If False, keeps as JSON.
        
    Returns:
        True if export was successful, False if no runs found.
    """
    latest_run = get_latest_run()
    if not latest_run:
        print("No runs found.")
        return False
    
    export_to_csv(
        output_file,
        run_name=latest_run,
        include_messages=include_messages,
        flatten_messages=flatten_messages
    )
    return True


def export_each_run_to_csv(
    output_dir: str,
    *,
    include_messages: bool = True,
    flatten_messages: bool = False,
    filename_template: str = "{run_name}.csv"
) -> List[Tuple[str, str]]:
    """
    Export each run to a separate CSV file.
    
    Args:
        output_dir: Directory where CSV files will be saved
        include_messages: Whether to include the conversation messages in the export
        flatten_messages: If True, converts messages to a single string. If False, keeps as JSON.
        filename_template: Template for CSV filenames. Use {run_name} as placeholder.
        
    Returns:
        List of tuples (run_name, csv_file_path) for successfully exported runs.
    """
    base_dir = redlite_data_dir()
    runs = list(read_runs(base_dir))
    
    if not runs:
        print("No runs found.")
        return []
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    exported_runs = []
    
    for run in runs:
        run_name = run["run"]
        # Clean run name for filename (replace problematic characters)
        safe_run_name = "".join(c if c.isalnum() or c in ('-', '_', '.') else '_' for c in run_name)
        csv_filename = filename_template.format(run_name=safe_run_name)
        csv_path = os.path.join(output_dir, csv_filename)
        
        try:
            _export_single_run_to_csv(
                base_dir, run_name, csv_path, include_messages, flatten_messages
            )
            exported_runs.append((run_name, csv_path))
            print(f"Exported run '{run_name}' to {csv_path}")
        except Exception as e:
            print(f"Failed to export run '{run_name}': {e}")
    
    print(f"Successfully exported {len(exported_runs)} runs to {output_dir}")
    return exported_runs


def export_to_csv(
    output_file: str,
    *,
    run_name: Optional[str] = None,
    include_messages: bool = True,
    flatten_messages: bool = False
) -> None:
    """
    Export RedLite run data to CSV format.
    
    Args:
        output_file: Path to the output CSV file
        run_name: Name of specific run to export. If None, exports all runs.
        include_messages: Whether to include the conversation messages in the export
        flatten_messages: If True, converts messages to a single string. If False, keeps as JSON.
    """
    base_dir = redlite_data_dir()
    
    if run_name:
        # Export specific run
        _export_single_run_to_csv(base_dir, run_name, output_file, include_messages, flatten_messages)
    else:
        # Export all runs
        _export_all_runs_to_csv(base_dir, output_file, include_messages, flatten_messages)


def _export_single_run_to_csv(
    base_dir: str,
    run_name: str,
    output_file: str,
    include_messages: bool,
    flatten_messages: bool
) -> None:
    """Export a single run to CSV."""
    try:
        meta = read_meta(base_dir, run_name)
        data = list(read_data(base_dir, run_name))
        
        if not data:
            print(f"No data found for run: {run_name}")
            return
            
        print(f"Exporting run '{run_name}' with {len(data)} records to {output_file}")
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = _get_fieldnames(data[0], meta, include_messages)
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for item in data:
                row = _prepare_row(item, meta, include_messages, flatten_messages)
                writer.writerow(row)
                
    except FileNotFoundError:
        print(f"Run '{run_name}' not found.")
    except Exception as e:
        print(f"Error exporting run '{run_name}': {e}")


def _export_all_runs_to_csv(
    base_dir: str,
    output_file: str,
    include_messages: bool,
    flatten_messages: bool
) -> None:
    """Export all runs to a single CSV file."""
    runs = list(read_runs(base_dir))
    
    if not runs:
        print("No runs found.")
        return
    
    print(f"Exporting {len(runs)} runs to {output_file}")
    
    all_data = []
    for run in runs:
        try:
            meta = read_meta(base_dir, run["run"])
            data = list(read_data(base_dir, run["run"]))
            
            for item in data:
                row = _prepare_row(item, meta, include_messages, flatten_messages)
                all_data.append(row)
                
        except Exception as e:
            print(f"Warning: Could not read run '{run['run']}': {e}")
            continue
    
    if not all_data:
        print("No data found in any runs.")
        return
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = _get_fieldnames(all_data[0], None, include_messages)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in all_data:
            writer.writerow(row)
    
    print(f"Exported {len(all_data)} records from {len(runs)} runs.")


def _get_fieldnames(sample_row: dict, meta: Optional[Run], include_messages: bool) -> List[str]:
    """Get CSV fieldnames based on the data structure."""
    base_fields = ["run_name", "dataset", "model", "metric", "id"]
    
    if include_messages:
        base_fields.append("messages")
    
    base_fields.extend(["expected", "actual", "score"])
    
    # Add any additional fields that might be present (but skip messages if not including them)
    for key in sample_row.keys():
        if key not in base_fields and (include_messages or key != "messages"):
            base_fields.append(key)
    
    return base_fields


def _prepare_row(
    item: dict,
    meta: Run,
    include_messages: bool,
    flatten_messages: bool
) -> dict:
    """Prepare a data row for CSV export."""
    row = {
        "run_name": meta["run"],
        "dataset": meta["dataset"],
        "model": meta["model"],
        "metric": meta["metric"],
        "id": item.get("id", ""),
        "expected": item.get("expected", ""),
        "actual": item.get("actual", ""),
        "score": item.get("score", ""),
    }
    
    if include_messages and "messages" in item:
        if flatten_messages:
            # Convert messages to a readable string format
            messages = item["messages"]
            flattened = []
            for msg in messages:
                role = msg.get("role", "")
                content = msg.get("content", "")
                flattened.append(f"{role}: {content}")
            row["messages"] = " | ".join(flattened)
        else:
            # Keep as JSON string
            row["messages"] = json.dumps(item["messages"])
    
    # Add any additional fields from the item (but skip messages if not including them)
    for key, value in item.items():
        if key not in row and (include_messages or key != "messages"):
            row[key] = value
    
    return row


def list_runs() -> None:
    """List all available runs."""
    base_dir = redlite_data_dir()
    runs = list(read_runs(base_dir))
    
    if not runs:
        print("No runs found.")
        return
    
    print(f"Found {len(runs)} runs:")
    print(f"{'Run Name':<30} {'Dataset':<25} {'Model':<20} {'Metric':<15} {'Records'}")
    print("-" * 95)
    
    for run in runs:
        try:
            data_count = len(list(read_data(base_dir, run["run"])))
            print(f"{run['run']:<30} {run['dataset']:<25} {run['model']:<20} {run['metric']:<15} {data_count}")
        except Exception:
            print(f"{run['run']:<30} {run['dataset']:<25} {run['model']:<20} {run['metric']:<15} Error")
