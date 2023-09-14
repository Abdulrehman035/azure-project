import csv
import json

def csv_to_json_with_skip(csv_filename):
    json_data = []
    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader):
            if index % 2 == 0:
                json_data.append(json.dumps(row))
    return json_data

csv_filename = "dataset/1_Bitcoin.csv" 
json_rows = csv_to_json_with_skip(csv_filename)
for json_row in json_rows:
    print(json_row)
