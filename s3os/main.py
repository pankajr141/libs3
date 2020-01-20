import boto3

class os():
    def __init__(self):
        pass

    def authorize(self, bucket, aws_access_key_id=None, aws_secret_access_key=None):
        self.s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.bucket = self.s3.Bucket(bucket)
    
    def listdir(self, directory):
        if directory.startswith("\\") or directory.startswith("/"):
            directory = directory[1:]
        print(directory)
        for bucket_object in self.bucket.objects.filter(Prefix=directory, Delimiter='/'):
            print(bucket_object.key)