import boto3

def Shutil():
    def authorize(self, bucket, aws_access_key_id=None, aws_secret_access_key=None):
        self.s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.bucket = self.s3.Bucket(bucket)

    def copy(self, src, dst):
        raise Exception("Not implemented in this version")
        
    def copytree(self):
        raise Exception("Not implemented in this version")

    def rmtree(self):
        raise Exception("Not implemented in this version")
        
    def move(self):
        raise Exception("Not implemented in this version")
        
    def make_archive(self):
        raise Exception("Not implemented in this version")

