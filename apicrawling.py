import requests, json, time, os
url = 'http://apis.data.go.kr/B551172/CancerScreenorCohortStatusService/getCancerScreenorCohort'

sub = {
'CancerIncCnt',
'DeadCnt',
'AgeSexInfo',
'BodyMeasmntAvgInfo',
'GeneralBldTestAvgInfo',
'TumorMarkerAvgInfo',
'GeneralChemAvgInfo',
}

params ={'serviceKey' : 'NGM9g1OzpPvWSeMDkkuWBjDVdLC4fhGD5zPVjvg8nrl/WTJScfQlqMfdHDP3U37ZXo/DCVeXmM5AppVRUjMk3g==', 'pageNo' : '1', 'numOfRows' : '500', 'resultType' : 'json' }

# 최대 재시도 횟수 설정
max_retries = 5

# 데이터를 저장할 폴더 생성
if not os.path.exists('data'):
    os.makedirs('data')

for i in sub:
    url_name = url + i
    
    # 재시도 횟수 초기화
    retries = 0
    
    while retries < max_retries:
        try:
            response = requests.get(url_name, params=params)
            with open(os.path.join('data', i + '.json'), 'w', encoding='utf-8') as f:
                json.dump(response.json(), f, ensure_ascii=False, indent=4)
            # 성공했으므로 루프를 빠져나옴
            break
        except json.decoder.JSONDecodeError:
            # 재시도 횟수 증가
            retries += 1
            # 잠시 대기한 후 재시도
            time.sleep(1)