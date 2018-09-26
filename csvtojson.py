import json
import csv
"""
# Copyright (c) 2018 Aquafortis
# https://github.com/Aquafortis/json-csv-converter
# $ python3 csvtojson.py
"""
class CsvJson(object):

    def csv_to_json(self):

        csvrows = []
        csvfile = open("input.csv", "r")
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csvrows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        csvfile.close()
        jsonfile = open("output.json", "w")
        data = csvrows
        poetize = jsonfile.write(json.dumps(data, indent=4))
        jsonfile.close()

CsvJson().csv_to_json()
