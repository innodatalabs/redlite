def main():
    import argparse

    parser = argparse.ArgumentParser(prog="redlite", description="CLI ops for redlite")
    subparsers = parser.add_subparsers(required=True, dest="cmd")

    parser_server = subparsers.add_parser("server", help="starts UI server")
    parser_server.add_argument("--port", "-p", type=int, default=8000, help="Server port")
    parser_server.add_argument("--skin", "-s", type=str, default="default", help="UI skin")

    parser_server_freeze = subparsers.add_parser(
        "server-freeze", help="generates files for a static website serving data"
    )
    parser_server_freeze.add_argument("outdir", type=str, help="Output directory")
    parser_server_freeze.add_argument("--skin", "-s", type=str, default="default", help="UI skin")

    parser_server= subparsers.add_parser("upload", help="Uploads all tasks to ZenoML (for review and analysis)")
    parser_server.add_argument("--api-key", "-k", help="Zeno API key (if not set, must be in ZENO_API_KEY env)")
    parser_server.add_argument(
        "--zeno-project", "-z", default="redlite", help='Name of the target Zeno project. Default is "redlite"'
    )

    parser_export = subparsers.add_parser("export", help="Export run data to CSV format")
    parser_export.add_argument("output", help="Output CSV file path")
    parser_export.add_argument("--run", "-r", help="Specific run name to export (if not provided, exports all runs)")
    parser_export.add_argument("--no-messages", action="store_true", help="Exclude conversation messages from export")
    parser_export.add_argument("--flatten-messages", action="store_true", help="Flatten messages to readable text instead of JSON")

    parser_export_latest = subparsers.add_parser("export-latest", help="Export the latest run to CSV format")
    parser_export_latest.add_argument("output", help="Output CSV file path")
    parser_export_latest.add_argument("--no-messages", action="store_true", help="Exclude conversation messages from export")
    parser_export_latest.add_argument("--flatten-messages", action="store_true", help="Flatten messages to readable text instead of JSON")

    parser_export_each = subparsers.add_parser("export-each", help="Export each run to separate CSV files")
    parser_export_each.add_argument("output_dir", help="Output directory for CSV files")
    parser_export_each.add_argument("--no-messages", action="store_true", help="Exclude conversation messages from export")
    parser_export_each.add_argument("--flatten-messages", action="store_true", help="Flatten messages to readable text instead of JSON")
    parser_export_each.add_argument("--template", default="{run_name}.csv", help="Filename template (default: {run_name}.csv)")

    parser_list = subparsers.add_parser("list", help="List all available runs")

    args = parser.parse_args()
    if args.cmd == "server":
        from .server._app import main as server_main

        print(f"*** HTTP UI server. Skin={args.skin}")
        server_main(args.port, skin=args.skin)

    elif args.cmd == "server-freeze":
        from .server._app import freeze as server_freeze
        import asyncio

        print(f"*** Freezing UI server to {args.outdir}. Skin={args.skin}")
        asyncio.run(server_freeze(args.outdir, skin=args.skin))

    elif args.cmd == "upload":
        from .zeno.upload import upload

        upload(
            api_key=args.api_key,
            zeno_project=args.zeno_project,
        )

    elif args.cmd == "export":
        from .export import export_to_csv

        export_to_csv(
            args.output,
            run_name=args.run,
            include_messages=not args.no_messages,
            flatten_messages=args.flatten_messages,
        )

    elif args.cmd == "export-latest":
        from .export import export_latest_run_to_csv

        success = export_latest_run_to_csv(
            args.output,
            include_messages=not args.no_messages,
            flatten_messages=args.flatten_messages,
        )
        if not success:
            exit(1)

    elif args.cmd == "export-each":
        from .export import export_each_run_to_csv

        exported_runs = export_each_run_to_csv(
            args.output_dir,
            include_messages=not args.no_messages,
            flatten_messages=args.flatten_messages,
            filename_template=args.template,
        )
        if not exported_runs:
            exit(1)

    elif args.cmd == "list":
        from .export import list_runs

        list_runs()


if __name__ == "__main__":
    main()
