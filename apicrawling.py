import requests, json, time, os

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

params ={'serviceKey' : 'NGM9g1OzpPvWSeMDkkuWBjDVdLC4fhGD5zPVjvg8nrl/WTJScfQlqMfdHDP3U37ZXo/DCVeXmM5AppVRUjMk3g==', 'numOfRows' : '100', 'centerNm' : '국립암센터', 'fromYear' : '1999', 'toYear' : '2018', 'type' : 'json' }

# 최대 재시도 횟수 설정
max_retries = 5

# 데이터를 저장할 폴더 생성
if not os.path.exists('data'):
    os.makedirs('data')

for i in sub:
    url_name = url + i
    json_data = []
    pagenum = 1
    # 재시도 횟수 초기화
    retries = 0
    print(url_name)
    
    while retries < max_retries:
        try:
            params['pageNo'] = '{}'.format(pagenum)
            response = requests.get(url_name, params=params)
            max_len = response.json()
            json_data.append(response.json())
            
            if (max_len['totalCount'] / 100) + 1 <= pagenum:
                json_data = json.dumps(json_data)
                
                file_path = os.path.join('data', i.replace('/', '-') + '.json')
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, ensure_ascii=True, indent=4)
                # 성공했으므로 루프를 빠져나옴
                print("{} 성공하였습니다".format(i))
                break
            pagenum += 1
        except json.decoder.JSONDecodeError:
            print("재시도 합니다.")
            # 재시도 횟수 증가
            retries += 1
            # 잠시 대기한 후 재시도
            time.sleep(1)