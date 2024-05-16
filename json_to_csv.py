import json
import csv
import glob
import os

'''
적용대상 파일 : 
    2-1. 암 종류별 흡연 여부(SMOKING_CANCER)
    2-2. 암 종류별 음주 여부(ALCH_CANCER)
'''
def type2_json_to_csv(json_file, csv_file):
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

'''
한글로 된 5개 json 파일에 대한 csv 변환 처리
'''
def other_json_to_csv(json_file, csv_file, fieldnames):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # CSV 파일로 쓰기
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)


def get_all_json_file():
    json_directory = 'data'
    json_files = glob.glob(os.path.join(json_directory, '*.json'))
    return json_files

# MAIN
if __name__ == '__main__':
    '''
    # 데이터 디렉터리 내의 모든 JSON 파일을 변환
    json_files = get_all_json_file()

    for json_file in json_files:
        csv_file = json_file.replace('.json', '.csv')
        print(f'Converting {json_file} to {csv_file}...')
        type2_json_to_csv(json_file, csv_file)
    '''

    # 5개 한글 json 파일 처리 : [파일명, 키(컬럼)이름]
    other_json_flies = [
        ["CANCER_BY_YEAR", ["cnacer_type", "incident_year", "total_cnt", "m_cnt", "f_cnt"]],
        ["ALCH_RATE_BY_YEAR", ["incident_year", "drinking_rate"]],
        ["SMOKING_RATE_BY_YEAR", ["incident_year", "smoking_rate"]],
        ["REGION_BY_AGE", ["region", "age_group", "year_2014", "year_2015", "year_2016", "year_2017", "year_2018"]],
        ["CANCER_BY_REGION", ["region", "total_cnt", "m_cnt", "f_cnt"]]
    ]
    for json_file in other_json_flies:
        json_file_name = 'data/' + json_file[0] + '.json'
        csv_file_name = 'data/' + json_file[0] + '.csv'
        other_json_to_csv(json_file_name, csv_file_name, json_file[1])