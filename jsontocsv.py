import json
import csv
"""
# Copyright (c) 2018 Aquafortis
# https://github.com/Aquafortis/json-csv-converter
# $ python3 jsontocsv.py
"""
def json_to_csv():
    jsonfile = open("input.json", "r")
    data = json.load(jsonfile)
    jsonfile.close()
    csvfile = open("output.csv", "w")
    written = csv.writer(csvfile)
    written.writerow(data[0].keys())
    for row in data:
        written.writerow(row.values())
    csvfile.close()
    return written
json_to_csv()
