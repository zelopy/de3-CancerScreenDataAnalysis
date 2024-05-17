import requests, json, time, os, csv

url = 'http://apis.data.go.kr/B551172/'

sub = {
'Colon04/voAlchbyType',
'Colon05/voSmokeByType',
'Colon06/voPastSmokeByType',
'Gastric04/gsAlchbyType',
'Gastric05/gsSmokeByType',
'Gastric06/gsPastSmokeByType',
'Liver04/lvAlchbyType',
'Liver05/lvSmokeByType',
'Liver06/lvPastSmokeByType',
'Cholan04/chAlchbyType',
'Cholan05/chSmokeByType',
'Cholan06/chPastSmokeByType',
'Pancreatic04/pnAlchbyType',
'Pancreatic05/pnSmokeByType',
'Pancreatic06/pnPastSmokeByType',
'Lung04/luAlchbyType',
'Lung05/luSmokeByType',
'Lung06/luPastSmokeByType',
'Prostate04/prAlchbyType',
'Prostate05/prSmokeByType',
'Prostate06/prPastSmokeByType',
'Kidney04/kiAlchbyType',
'Kidney05/kiSmokeByType',
'Kidney06/kiPastSmokeByType',
}

params ={'serviceKey' : 'NGM9g1OzpPvWSeMDkkuWBjDVdLC4fhGD5zPVjvg8nrl/WTJScfQlqMfdHDP3U37ZXo/DCVeXmM5AppVRUjMk3g==', 'numOfRows' : '100', 'centerNm' : '국립암센터', 'fromYear' : '2021', 'toYear' : '2021', 'type' : 'json' }

# 최대 재시도 횟수 설정
max_retries = 5

# 데이터를 저장할 폴더 생성
if not os.path.exists('data'):
    os.makedirs('data')

for i in sub:
    url_name = url + i
    json_data = []
    pagenum = 1
    retries = 0

    print(url_name)

    while retries < max_retries:
        params['pageNo'] = str(pagenum)  # 문자열 형변환

        try:
            response = requests.get(url_name, params=params)
            response.raise_for_status()  # HTTP 에러 발생 시 예외 발생

            data = response.json()
            json_data.extend(data.get('items', []))  # items 키가 없을 경우 빈 리스트 반환

            """#json파일로 저장하기
            total_count = data.get('totalCount', 0)
            if total_count <= pagenum * 100:  # 데이터 가져오기 완료
                file_path = os.path.join('data', i.replace('/', '-') + '.json')
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)
                print(f"{i} 성공하였습니다")
                break
            """
            
            #CSV파일로 저장하기
            total_count = data.get('totalCount', 0)
            if total_count <= pagenum * 100:  # 데이터 가져오기 완료
                file_path = os.path.join('data', i.replace('/', '-') + '.csv')

                # 테이블 순서에 맞는 필드 이름 설정
                fieldnames = ['statsMetaNo', 'centerNm', 'critYr', 'ptAge', 'ptSexCd', 'statsTrgtNm', 'ncsNmvl', 'wholNcsDnmvl', 'ptCntNmvl', 'wholPtCntDnmvl']

                with open(file_path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()  # 헤더 작성

                    # 데이터 행 작성 (필드 순서에 맞춰 데이터 추출)
                    for item in json_data:
                        ordered_item = {
                            'statsMetaNo': item['statsMetaNo'],
                            'centerNm': item['centerNm'],
                            'critYr': item['critYr'],
                            'ptAge': item['ptAge'],
                            'ptSexCd': item['ptSexCd'],
                            'statsTrgtNm': item['statsTrgtNm'],
                            'ncsNmvl': item['ncsNmvl'],
                            'wholNcsDnmvl': item['wholNcsDnmvl'],
                            'ptCntNmvl': item['ptCntNmvl'],
                            'wholPtCntDnmvl': item['wholPtCntDnmvl']
                        }
                        writer.writerow(ordered_item)

                print(f"{i} 성공하였습니다")
                break
            
            pagenum += 1

        except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError) as e:
            print(f"오류 발생: {e}, 재시도합니다.")
            retries += 1
            time.sleep(1)