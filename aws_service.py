import boto3
import json, os

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


if __name__ == '__main__':
    s3_client = s3_connection()
    upload_datafile_to_s3(s3_client)