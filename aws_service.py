import boto3
import json, os
import psycopg2
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

'''
S3 연결
    Returns : S3객체
'''
def s3_connection():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    key_file = os.path.join(BASE_DIR, 'de3-CancerScreenDataAnalysis', 'aws_info.json')
    print(os.path.realpath(key_file))
    try:
        with open(key_file) as f:
            config = json.load(f)
        access_key = config.get('ACCESS_KEY_ID', '')
        secret_key = config.get('SECRET_ACCESS_KEY', '')
    except FileNotFoundError:
        print('aws_info.json 파일이 존재하지 않습니다.')
    
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )
    except Exception as e:
        print(e)
    else:
        print("S3 버킷 연결 성공") 
        return s3
    
'''
data 폴더 내 파일 전체를 S3에 업로드
    Parameters : S3객체
'''
def upload_datafile_to_s3(s3_client):
    try:
        key_file = 'aws_info.json'
        with open(key_file) as f:
            config = json.load(f)
    except FileNotFoundError:
        print('aws_info.json 파일이 존재하지 않습니다.')
    
    # S3 버킷명
    s3_bucket_name = config.get('S3_BUCKET_NAME', '')

    try:
        # TODO : 업로드 테스트 : 정상
        # s3_client.upload_file("test.txt", s3_bucket_name, "test.txt")
        local_path = "data/"
        for file_name in os.listdir(local_path):
            print("Uploading: ", file_name)
            s3_client.upload_file(local_path + file_name, s3_bucket_name, file_name)
    except Exception as e:
        print(e)

# def copy_s3_to_redshift(redshift_client):
#     try:
#         key_file = 'aws_info.json'
#         with open(key_file) as f:
#             config = json.load(f)
#         access_key = config.get('ACCESS_KEY_ID', '')
#         secret_key = config.get('SECRET_ACCESS_KEY', '')
#     except FileNotFoundError:
#         print('aws_info.json 파일이 존재하지 않습니다.')

#     query = """
#         COPY table_name
#         FROM 's3파일위치'
#         ACCESS_KEY_ID '{}'
#         SECRET_ACCESS_KEY '{}'
#         JSON 'auto'
#     """.format(access_key, secret_key)

#     response = redshift_client.execute_statement(
#         ClusterIdentifier = '',
#         Database='dev',
#         Sql=query
#     )
#     print(response)


'''
Redshift DB 객체 생성
'''
def get_db_engine():
    # Redshift 연결 정보
    try:
        key_file = 'aws_info.json'
        with open(key_file) as f:
            config = json.load(f)
        
        db_user = config.get('REDSHIFT_ID', '')
        db_password = config.get('REDSHIFT_PW', '')
        db_host = config.get('REDSHIFT_ENDPOINT', '')
        
        # Redshift URL
        db_url = f'postgresql://{db_user}:{db_password}@{db_host}'

        # SQLAlchemy 엔진 생성
        engine = create_engine(db_url)

    except FileNotFoundError:
        print('aws_info.json 파일이 존재하지 않습니다.')
    return engine


'''
Redshift에 테이블 생성
'''
def create_table_in_redshift(engine):
    # TODO : TEST
    create_table_query = """
    CREATE TABLE raw_data.chAlchbyType (
        statsMetaNo VARCHAR(255),
        centerNm VARCHAR(255),
        critYr VARCHAR(4),
        ptAge VARCHAR(3),
        ptSexCd VARCHAR(1),
        statsTrgtNm VARCHAR(1),
        ncsNmvl VARCHAR(10),
        wholNcsDnmvl VARCHAR(10),
        ptCntNmvl VARCHAR(10),
        wholPtCntDnmvl VARCHAR(10)
    );
    """
    # SQL 실행
    with engine.connect() as connection:
        result = connection.execute(text(create_table_query))
        print("Table created:", result.rowcount == -1)


'''
S3에서 Redshift 테이블로 데이터 COPY
'''
def copy_s3_to_redshift(engine):
    # TODO : TEST
    data_copy_query = f"""
    COPY raw_data.chAlchbyType
    FROM 's3://de3-pjt2/copy_test.json'
    credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
    FORMAT AS JSON 's3://de3-pjt2/json_paths/jsonpath_file_AlchbyType.json'
    timeformat 'auto';
    """
    # SQL 실행
    with engine.connect() as connection:
        result = connection.execute(text(data_copy_query))
        print("Data copy : ", result.rowcount == -1)


# MAIN
if __name__ == '__main__':
    # S3 파일 업로드
    # s3_client = s3_connection()   # OK
    # upload_datafile_to_s3(s3_client)  # OK

    # S3 -> Redshift 파일 Copy
    engine = get_db_engine()
    # create_table_in_redshift(engine)  # OK
    copy_s3_to_redshift(engine) # TODO : json 포맷 관련 에러 발생...