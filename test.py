import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # CSV 파일로 쓰기
    with open(csv_file, 'w', newline='', encoding='cp949') as f:
        writer = csv.DictWriter(f, fieldnames=data['items'][0].keys())
        writer.writeheader()
        for item in data['items']:
            writer.writerow(item)

# JSON 파일 경로
json_file = 'data/BodyMeasmntAvgInfo.json'
# CSV 파일 경로
csv_file = 'data/BodyMeasmntAvgInfo.csv'

# 변환 실행
json_to_csv(json_file, csv_file)
