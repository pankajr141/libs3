import boto3


class Path():
    def __init__(self, os_obj):
        self.os_obj = os_obj
    
    def exists(self):
        raise Exception("Not implemented in this version")
    
    def dirname(self):
        raise Exception("Not implemented in this version")
        
    def basename(self):
        raise Exception("Not implemented in this version")

    def is_dir(self):
        raise Exception("Not implemented in this version")
    
    def is_file(self):
        raise Exception("Not implemented in this version")

class os():
    def __init__(self):
        self.path = Path(self)

    def authorize(self, bucket, aws_access_key_id=None, aws_secret_access_key=None):
        self.s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.bucket = self.s3.Bucket(bucket)
    
    def listdir(self, directory):
        if directory.startswith("\\") or directory.startswith("/"):
            directory = directory[1:]
        print(directory)
        for bucket_object in self.bucket.objects.filter(Prefix=directory, Delimiter='/'):
            print(bucket_object.key)

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
        
def shutil():
    def authorize(self, bucket, aws_access_key_id=None, aws_secret_access_key=None):
        self.s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.bucket = self.s3.Bucket(bucket)

    def copy(self, src, dst):
        ''' Not a OS function, but a shutil function adding to improve usage'''
        raise Exception("Not implemented in this version")