import csv
import json


def csv_to_json(input_file, output_file):
    with open(input_file, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Converted {input_file} to {output_file}")

def json_to_csv(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    if not data:
        print("JSON file is empty")
        return

    keys = data[0].keys()

    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Converted {input_file} to {output_file}")

def format_json(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Formatted {input_file} → {output_file}")