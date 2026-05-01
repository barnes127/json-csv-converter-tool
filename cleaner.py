import csv


def remove_duplicates(input_file, output_file):
    with open(input_file, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    seen = set()
    unique_rows = []

    for row in rows:
        row_tuple = tuple(row.items())
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(row)

    if not unique_rows:
        print("No data found")
        return

    keys = unique_rows[0].keys()

    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(unique_rows)

    print(f"Removed duplicates → {output_file}")

def sort_csv(input_file, output_file, column_name):
    with open(input_file, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    if not rows:
        print("No data found")
        return

    if column_name not in rows[0]:
        print(f"Column '{column_name}' not found")
        return

    sorted_rows = sorted(rows, key=lambda row: row[column_name])

    keys = rows[0].keys()

    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(sorted_rows)

    print(f"Sorted {input_file} by '{column_name}' → {output_file}")