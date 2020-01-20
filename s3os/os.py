import boto3
from s3os import path

class OS():
    def __init__(self):
        self.path = path.Path(self)

    def authorize(self, bucket, aws_access_key_id=None, aws_secret_access_key=None):
        self.s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.bucket = self.s3.Bucket(bucket)

    def __listdir(self, directory):
        if directory.startswith("\\") or directory.startswith("/"):
            directory = directory[1:]
#         for bucket_object in self.bucket.objects.filter(Prefix=directory, Delimiter='/'):
        for bucket_object in self.bucket.objects.filter(Prefix=directory):
            yield bucket_object.key

    def listdir(self, directory):        
        return list(self.__listdir(directory))

    def walk(self):
        raise Exception("Not implemented in this version")

    def mkdir(self):
        raise Exception("Not implemented in this version")
    
    def makedirs(self):
        raise Exception("Not implemented in this version")

    def scandir(self):
        raise Exception("Not implemented in this version")

    def remove(self):
        raise Exception("Not implemented in this version")

    def rmdir(self):
        raise Exception("Not implemented in this version")
        
    def unlink(self):
        raise Exception("Not implemented in this version")