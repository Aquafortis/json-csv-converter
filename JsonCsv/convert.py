import json
import csv
"""
# Copyright (c) 2023 Aquafortis
# https://github.com/Aquafortis/json-csv-converter
# $ python3 convert.py
"""
while True:

    try:

        fileType = input("File type to convert from, json or csv ?: ")

        if fileType.lower() == "json":

            inputFile = input("Drag json file here, clear trailing whitespace, and hit enter:\n>>> ")

            if inputFile.endswith((".json", ".txt")):

                jsonfile = open(inputFile)
                data = json.load(jsonfile)
                jsonfile.close()
                csvfile = open("output.csv", "w")
                poetize = csv.writer(csvfile)
                poetize.writerow(data[0].keys())
                for row in data:
                    poetize.writerow(row.values())
                csvfile.close()
                print("Converted to output.csv")
                print("----------")

            else:
                print("Incorrect file type!")
                print("----------")

        elif fileType.lower() == "csv":

            inputFile = input("Drag csv file here, clear trailing whitespace, and hit enter:\n>>> ")

            if inputFile.endswith((".csv", ".txt")):

                csvrows = []
                csvfile = open(inputFile)
                reader = csv.DictReader(csvfile)
                title = reader.fieldnames
                for row in reader:
                    csvrows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
                csvfile.close()
                jsonfile = open("output.json", "w")
                data = csvrows
                poetize = jsonfile.write(json.dumps(data, indent=4))
                jsonfile.close()
                print("Converted to output.json")
                print("----------")

            else:
                print("Incorrect file type!")
                print("----------")

        else:
            print("No file type specified!")
            print("----------")

    except Exception as e:
        print("----------")
        print("Error:", e)
        print("Check the file and try again ...")
        print("----------")

# Use Ctrl + C or control + C etc. to exit
