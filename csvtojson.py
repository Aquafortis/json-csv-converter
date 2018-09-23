import json
import csv
"""
# Copyright (c) 2018 Aquafortis
# https://github.com/Aquafortis/json-csv-converter
# $ python3 csvtojson.py
"""
def csv_to_json():
    csvrows = []
    csvfile = open("input.csv", "r")
    reader = csv.DictReader(csvfile)
    title = reader.fieldnames
    for row in reader:
        csvrows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
    csvfile.close()
    jsonfile = open("output.json", "w")
    data = csvrows
    written = jsonfile.write(json.dumps(data, indent=4))
    jsonfile.close()
    return written
csv_to_json()
