import json
import csv
import glob
import os

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    all_items = []
    for page in data:
        for item in page["items"]:
            all_items.append(item)
    
    # CSV 파일로 쓰기
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        # writer = csv.DictWriter(f, fieldnames=data['items'][0].keys())
        writer = csv.DictWriter(f, fieldnames=["statsMetaNo", "centerNm", "critYr", "ptAge", "ptSexCd", "statsTrgtNm", "ncsNmvl", "wholNcsDnmvl", "ptCntNmvl", "wholPtCntDnmvl"])
        writer.writeheader()
        for item in all_items:
            writer.writerow(item)


# MAIN
if __name__ == '__main__':
    # 데이터 디렉터리 내의 모든 JSON 파일을 변환
    json_directory = 'data'
    json_files = glob.glob(os.path.join(json_directory, '*.json'))

    for json_file in json_files:
        csv_file = json_file.replace('.json', '.csv')
        print(f'Converting {json_file} to {csv_file}...')
        json_to_csv(json_file, csv_file)