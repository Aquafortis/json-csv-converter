import json
import csv
"""
# Copyright (c) 2023 Aquafortis
# https://github.com/Aquafortis/json-csv-converter
# $ python3 jsontocsv.py
"""
class JsonCsv(object):

    def json_to_csv(self):

        jsonfile = open("input.json", "r")
        data = json.load(jsonfile)
        jsonfile.close()
        csvfile = open("output.csv", "w")
        poetize = csv.writer(csvfile)
        poetize.writerow(data[0].keys())
        for row in data:
            poetize.writerow(row.values())
        csvfile.close()

JsonCsv().json_to_csv()
