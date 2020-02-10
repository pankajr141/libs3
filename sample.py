import sys
import boto3
import os as base_os
def main(bucket, aws_access_key_id, aws_secret_access_key):
    print("=========================")
    from libs3 import os
    os.authorize(bucket, aws_access_key_id, aws_secret_access_key)

    print(os.listdir("/"))
    print(os.listdir("/dir_1/dir_1/"))
    print(os.listdir("/dir_1/dir_1", filesonly=True))
    
    print(os.path.exists('/dir_1/file_2'))
    print(os.path.isfile('/dir_1/file_2'))
    print(os.path.isdir('/dir_1/file_2'))
    print(os.path.basename('/dir_1/file_2'))
    print(os.path.dirname('/dir_1/file_2'))

    print("=========================")    
    from libs3 import shutil

    shutil.authorize(bucket, aws_access_key_id, aws_secret_access_key)
    shutil.copy("/dir_1/file_3", "localfile", download=True)
    shutil.copy("localfile", "/dir_2", upload=True)

    print(os.listdir("/dir_2"))
    print(base_os.path.exists("localfile"))

if __name__ == "__main__":
    try:
        bucket = sys.argv[1]
        aws_access_key_id = sys.argv[2]
        aws_secret_access_key = sys.argv[3]
        main(bucket, aws_access_key_id, aws_secret_access_key)
    except Exception as err:
        print(err)
