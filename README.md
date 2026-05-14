# JSON / CSV Converter Tool

A simple CLI tool for converting and cleaning data files.

## Features

- CSV → JSON
- JSON → CSV
- Format JSON files
- Remove duplicate CSV rows
- Sort CSV by column

## Usage

### CSV to JSON
```bash
python3 main.py csv-to-json input.csv output.json

python3 main.py json-to-csv input.json output.csv

python3 main.py format-json input.json output.json

python3 main.py dedupe input.csv output.csv

python3 main.py sort input.csv output.csv --column column_name