import sys
import boto3
import os as base_os
def main(bucket, aws_access_key_id, aws_secret_access_key):
    print("=========================")
    from libs3 import os
    os.authorize(bucket, aws_access_key_id, aws_secret_access_key)

    print(os.listdir("/"))
    #print(os.listdir("/dir_1/dir_1/"))
    print(os.listdir("/dir_2/dir_1", filesonly=True))
    
    print(os.path.exists('/dir_2/file_2'))
    print(os.path.isfile('/dir_2/file_2'))
    print(os.path.isdir('/dir_2/dir_1'))
    print(os.path.basename('/dir_2/file_2'))
    print(os.path.dirname('/dir_2/file_2'))
    
    print("=========================")    
    from libs3 import shutil
    shutil.authorize(bucket, aws_access_key_id, aws_secret_access_key)
    
    print("Testing shutil.copy")
    shutil.copy("/dir_2/file_1", "/dir_2/cold/sdfe/fef") # Copy within s3
    shutil.copy("/dir_2/file_1", "/dir_2/file_1_cp") # Copy within s3
    shutil.copy("/dir_2/file_1", "localfile", download=True) #Copy from s3 to local
    shutil.copy("localfile", "/dir_2/l", upload=True)  # Copuy from local to s3

    print("Testing shutil.copyfile")
    #shutil.copyfile("/dir_2/file_1", "/dir_2/dir_1") # Copy within s3
    shutil.copyfile("/dir_2/file_1", "/dir_2/file_ks") # Copy within s3
    shutil.rmtree('/dir_2/cold')
    shutil.move('/dir_2/file_1_cp', '/dir_2/file_1_moved')

    os.remove('/dir_2/file_ks')
    print(os.listdir("/dir_2"))

if __name__ == "__main__":
    try:
        bucket = sys.argv[1]
        aws_access_key_id = sys.argv[2]
        aws_secret_access_key = sys.argv[3]
        main(bucket, aws_access_key_id, aws_secret_access_key)
    except Exception as err:
        print(err)
