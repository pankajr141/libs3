import boto3

class Shutil():
    def __init__(self, os):
        self.os = os

    def authorize(self, bucket, aws_access_key_id=None, aws_secret_access_key=None):
        self.s3_r = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.s3_c = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.bucketname = bucket
        self.bucket = self.s3_r.Bucket(bucket)

    def copy(self, src, dst, upload=False, download=False):
        '''
        Copy files from src to dst. Below options are availaible
        when both src and dst are s3    - upload=False, download=False [Default]
        when src is local and dst is s3 - upload=True, download=False
        when src is s3 and dsr is local - upload=False, download=True

        '''
        if upload == False and src.startswith("/"):
            src = src[1:]
        if download == False and dst.startswith("/"):
            dst = dst[1:]

        if all([upload, download]):
            raise Exception("Both upload and download cannot be set as true")
        elif not any([upload, download]):
            self.s3_r.Object(self.bucketname, dst).copy_from(CopySource=self.bucketname+"/"+src)
            self.s3_r.Object(self.bucketname, src).delete()
        elif download:
            self.s3_c.download_file(self.bucketname, src, dst)
        elif upload:
            if self.os.path.isdir("/" + dst):
                dst = dst.rstrip("/") + "/" + self.os.path.basename(src)
            self.s3_c.upload_file(src, self.bucketname, dst)

    def copytree(self):
        raise Exception("Not implemented in this version")

    def rmtree(self):
        raise Exception("Not implemented in this version")
        
    def move(self):
        raise Exception("Not implemented in this version")
        
    def make_archive(self):
        raise Exception("Not implemented in this version")

