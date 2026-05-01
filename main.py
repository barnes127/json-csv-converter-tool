import argparse
from converter import csv_to_json, json_to_csv, format_json
from cleaner import remove_duplicates, sort_csv


def main():
    parser = argparse.ArgumentParser(
        description="JSON / CSV Converter Tool"
    )

    parser.add_argument(
        "command",
        choices=["csv-to-json", "json-to-csv", "format-json", "dedupe", "sort"],
        help="Command to run"
    )

    parser.add_argument(
        "input_file",
        help="Path to input file"
    )

    parser.add_argument(
        "output_file",
        help="Path to output file"
    )


    parser.add_argument(
        "--column",
        help="Column name to sort by"
    )

    args = parser.parse_args()

    if args.command == "csv-to-json":
        csv_to_json(args.input_file, args.output_file)

    if args.command == "json-to-csv":
        json_to_csv(args.input_file, args.output_file)

    if args.command == "format-json":
        format_json(args.input_file, args.output_file)

    if args.command == "dedupe":
        remove_duplicates(args.input_file, args.output_file)

    if args.command == "sort":
        if not args.column:
            print("Please provide a column name using --column")
            return

        sort_csv(args.input_file, args.output_file, args.column)

if __name__ == "__main__":
    main()