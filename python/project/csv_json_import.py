import csv
import json

csv_file = 'arin_2020.csv'
json_file = 'arin_2020.json'

# CSV 파일 읽기
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# JSON 파일 쓰기
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=4)
