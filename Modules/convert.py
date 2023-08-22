import json
import csv

def csv_to_json(csvFile, jsonFile):
    jsonArray = []

    with open(csvFile, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf, delimiter=';') #delimeter ;

        for row in csvReader:
            jsonArray.append(row)

    with open(jsonFile, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False).encode('utf8') #encode musi byt, jinak by to nevypisovalo s hackama
        jsonf.write(jsonString.decode('utf8'))

csvFile = r'C:\Users\toust\Downloads\rozvrh.csv' #mozna by slo zmenit na relativni cestu
jsonFile = r'data.json'
