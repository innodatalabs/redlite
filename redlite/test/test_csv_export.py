"""Tests for CSV export functionality."""

import csv
import json
import os
import tempfile
import unittest
from unittest.mock import patch, MagicMock
from typing import cast

from redlite.export import (
    export_to_csv, list_runs, _prepare_row, _get_fieldnames,
    get_latest_run, export_latest_run_to_csv, export_each_run_to_csv
)
from redlite._core import Run


class TestCSVExport(unittest.TestCase):
    """Test cases for CSV export functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_run_meta = cast(Run, {
            "run": "test-run-1",
            "dataset": "test-dataset", 
            "model": "test-model",
            "metric": "test-metric",
            "split": "test",
            "dataset_labels": {},
            "data_digest": "abc123",
            "max_samples": 0,
            "started": "2024-01-01T00:00:00Z",
            "completed": "2024-01-01T00:01:00Z",
            "duration": 60.0,
            "score_summary": {"count": 2, "mean": 0.75, "min": 0.5, "max": 1.0}
        })
        
        self.test_data = [
            {
                "id": "item1",
                "messages": [{"role": "user", "content": "Hello"}],
                "expected": "Hi there",
                "actual": "Hello back",
                "score": 0.8
            },
            {
                "id": "item2", 
                "messages": [{"role": "user", "content": "How are you?"}],
                "expected": "I'm fine",
                "actual": "Good thanks",
                "score": 0.7
            }
        ]

    def test_prepare_row_with_messages(self):
        """Test row preparation with messages included."""
        item = self.test_data[0]
        row = _prepare_row(item, self.test_run_meta, include_messages=True, flatten_messages=False)
        
        self.assertEqual(row["run_name"], "test-run-1")
        self.assertEqual(row["dataset"], "test-dataset")
        self.assertEqual(row["model"], "test-model")
        self.assertEqual(row["metric"], "test-metric")
        self.assertEqual(row["id"], "item1")
        self.assertEqual(row["expected"], "Hi there")
        self.assertEqual(row["actual"], "Hello back")
        self.assertEqual(row["score"], 0.8)
        self.assertEqual(row["messages"], json.dumps([{"role": "user", "content": "Hello"}]))

    def test_prepare_row_without_messages(self):
        """Test row preparation without messages."""
        item = self.test_data[0]
        row = _prepare_row(item, self.test_run_meta, include_messages=False, flatten_messages=False)
        
        self.assertEqual(row["run_name"], "test-run-1")
        self.assertNotIn("messages", row)

    def test_prepare_row_flattened_messages(self):
        """Test row preparation with flattened messages."""
        item = self.test_data[0]
        row = _prepare_row(item, self.test_run_meta, include_messages=True, flatten_messages=True)
        
        self.assertEqual(row["messages"], "user: Hello")

    def test_prepare_row_flattened_multi_messages(self):
        """Test row preparation with multiple flattened messages."""
        item = {
            "id": "item1",
            "messages": [
                {"role": "system", "content": "You are helpful"}, 
                {"role": "user", "content": "Hello"},
                {"role": "assistant", "content": "Hi"}
            ],
            "expected": "Hi there",
            "actual": "Hello back", 
            "score": 0.8
        }
        row = _prepare_row(item, self.test_run_meta, include_messages=True, flatten_messages=True)
        
        expected = "system: You are helpful | user: Hello | assistant: Hi"
        self.assertEqual(row["messages"], expected)

    def test_get_fieldnames_with_messages(self):
        """Test fieldname generation with messages."""
        sample_row = {
            "run_name": "test", "dataset": "test", "model": "test", "metric": "test",
            "id": "test", "messages": "test", "expected": "test", "actual": "test", "score": 0.8
        }
        
        fieldnames = _get_fieldnames(sample_row, self.test_run_meta, include_messages=True)
        expected = ["run_name", "dataset", "model", "metric", "id", "messages", "expected", "actual", "score"]
        self.assertEqual(fieldnames, expected)

    def test_get_fieldnames_without_messages(self):
        """Test fieldname generation without messages."""
        sample_row = {
            "run_name": "test", "dataset": "test", "model": "test", "metric": "test", 
            "id": "test", "messages": "test", "expected": "test", "actual": "test", "score": 0.8
        }
        
        fieldnames = _get_fieldnames(sample_row, self.test_run_meta, include_messages=False)
        expected = ["run_name", "dataset", "model", "metric", "id", "expected", "actual", "score"]
        self.assertEqual(fieldnames, expected)

    @patch('redlite.export.read_runs')
    def test_list_runs_empty(self, mock_read_runs):
        """Test list_runs with no runs."""
        mock_read_runs.return_value = []
        
        with patch('builtins.print') as mock_print:
            list_runs()
            mock_print.assert_called_with("No runs found.")

    @patch('redlite.export.read_runs')
    @patch('redlite.export.read_data')
    def test_list_runs_with_data(self, mock_read_data, mock_read_runs):
        """Test list_runs with run data."""
        mock_read_runs.return_value = [self.test_run_meta]
        mock_read_data.return_value = self.test_data
        
        with patch('builtins.print') as mock_print:
            list_runs()
            # Check that run information was printed
            self.assertTrue(any("test-run-1" in str(call) for call in mock_print.call_args_list))

    @patch('redlite.export.read_meta')
    @patch('redlite.export.read_data') 
    def test_export_single_run_to_csv(self, mock_read_data, mock_read_meta):
        """Test exporting a single run to CSV."""
        mock_read_meta.return_value = self.test_run_meta
        mock_read_data.return_value = self.test_data
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            csv_file = f.name
        
        try:
            export_to_csv(csv_file, run_name="test-run-1")
            
            # Verify CSV was created and has correct content
            self.assertTrue(os.path.exists(csv_file))
            
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]['run_name'], 'test-run-1')
            self.assertEqual(rows[0]['id'], 'item1')
            self.assertEqual(rows[1]['id'], 'item2')
            
        finally:
            if os.path.exists(csv_file):
                os.unlink(csv_file)

    @patch('redlite.export.read_runs')
    @patch('redlite.export.read_meta')
    @patch('redlite.export.read_data')
    def test_export_all_runs_to_csv(self, mock_read_data, mock_read_meta, mock_read_runs):
        """Test exporting all runs to CSV."""
        mock_read_runs.return_value = [self.test_run_meta]
        mock_read_meta.return_value = self.test_run_meta
        mock_read_data.return_value = self.test_data
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            csv_file = f.name
        
        try:
            export_to_csv(csv_file)
            
            # Verify CSV was created and has correct content
            self.assertTrue(os.path.exists(csv_file))
            
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]['run_name'], 'test-run-1')
            
        finally:
            if os.path.exists(csv_file):
                os.unlink(csv_file)

    @patch('redlite.export.read_runs')
    def test_get_latest_run_empty(self, mock_read_runs):
        """Test get_latest_run with no runs."""
        mock_read_runs.return_value = []
        
        result = get_latest_run()
        self.assertIsNone(result)

    @patch('redlite.export.read_runs')
    def test_get_latest_run_with_data(self, mock_read_runs):
        """Test get_latest_run with multiple runs."""
        run1 = self.test_run_meta.copy()
        run1["completed"] = "2024-01-01T10:00:00Z"
        run1["run"] = "older-run"
        
        run2 = self.test_run_meta.copy()
        run2["completed"] = "2024-01-01T12:00:00Z"
        run2["run"] = "newer-run"
        
        mock_read_runs.return_value = [run1, run2]
        
        result = get_latest_run()
        self.assertEqual(result, "newer-run")

    @patch('redlite.export.export_to_csv')
    @patch('redlite.export.get_latest_run')
    def test_export_latest_run_success(self, mock_get_latest, mock_export):
        """Test export_latest_run_to_csv with successful export."""
        mock_get_latest.return_value = "test-run"
        
        result = export_latest_run_to_csv("output.csv")
        
        self.assertTrue(result)
        mock_export.assert_called_once_with(
            "output.csv",
            run_name="test-run",
            include_messages=True,
            flatten_messages=False
        )

    @patch('redlite.export.get_latest_run')
    def test_export_latest_run_no_runs(self, mock_get_latest):
        """Test export_latest_run_to_csv with no runs."""
        mock_get_latest.return_value = None
        
        with patch('builtins.print') as mock_print:
            result = export_latest_run_to_csv("output.csv")
            
        self.assertFalse(result)
        mock_print.assert_called_with("No runs found.")

    @patch('redlite.export.read_runs')
    @patch('redlite.export._export_single_run_to_csv')
    @patch('os.makedirs')
    def test_export_each_run_success(self, mock_makedirs, mock_export_single, mock_read_runs):
        """Test export_each_run_to_csv with successful exports."""
        run1 = self.test_run_meta.copy()
        run1["run"] = "run-1"
        run2 = self.test_run_meta.copy()  
        run2["run"] = "run-2"
        
        mock_read_runs.return_value = [run1, run2]
        
        with patch('builtins.print'):
            result = export_each_run_to_csv("output_dir")
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], "run-1")
        self.assertEqual(result[1][0], "run-2")
        mock_makedirs.assert_called_once_with("output_dir", exist_ok=True)
        self.assertEqual(mock_export_single.call_count, 2)

    @patch('redlite.export.read_runs')
    def test_export_each_run_no_runs(self, mock_read_runs):
        """Test export_each_run_to_csv with no runs."""
        mock_read_runs.return_value = []
        
        with patch('builtins.print') as mock_print:
            result = export_each_run_to_csv("output_dir")
        
        self.assertEqual(result, [])
        mock_print.assert_called_with("No runs found.")


if __name__ == '__main__':
    unittest.main()
