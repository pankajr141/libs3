import boto3
import os as base_os

class Shutil():
    def __init__(self, os):
        self.os = os

    def authorize(self, bucketname, aws_access_key_id=None, aws_secret_access_key=None):
        self.s3_r = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.s3_c = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.bucketname = bucketname
        self.bucket = self.s3_r.Bucket(bucketname)

    def copy(self, src, dst, upload=False, download=False):
        '''
        Copy files from src to dst.

        Restrictions
        ============
        1. src - file only
        2. dst - file or directory

        Below options are availaible
        ============================
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
            if not self.os.path.exists(src):
                raise Exception("src (%s) does not exists in s3" % ("/" + src))
            if self.os.path.isdir("/" + src):
                raise Exception("src (%s) cannot be a directory" % ("/" + src))
#             We can also throw exception, if parent directory not present, lets just ignore now
#             if not self.os.path.exists(self.os.path.dirname("/" + dst)):
#                 raise Exception("Parent directory not present %s" % (self.os.path.dirname("/" + dst)))
            if self.os.path.isdir("/" + dst):
                dst = dst.rstrip("/") + "/" + self.os.path.basename(src)
            self.s3_r.Object(self.bucketname, dst).copy_from(CopySource=self.bucketname+"/"+src)

        elif download:
            if not self.os.path.exists(src):
                raise Exception("src (%s) does not exists in s3" % ("/" + src))
            if self.os.path.isdir("/" + src):
                raise Exception("src (%s) cannot be a directory" % ("/" + src))
            if base_os.path.isdir(dst):
                dst = dst.rstrip("/") + "/" + basename(src)
            self.s3_c.download_file(self.bucketname, src, dst)

        elif upload:
            if not base_os.path.exists(src):
                raise Exception("src (%s) does not exists in local" % (src))
            if base_os.path.isdir(src):
                raise Exception("src (%s) cannot be a directory" % (src))
#             if not self.os.path.exists(self.os.path.dirname("/" + dst)):
#                 raise Exception("Parent directory not present %s" % (self.os.path.dirname("/" + dst)))
            if self.os.path.isdir("/" + dst):
                dst = dst.rstrip("/") + "/" + self.os.path.basename(src)
            self.s3_c.upload_file(src, self.bucketname, dst)

    def copyfile(self, src, dst, upload=False, download=False):
        '''
        Copy files from src to dst.

        Restrictions
        ============
        1. src - file only
        2. dst - file only

        Below options are availaible
        ============================
        when both src and dst are s3    - upload=False, download=False [Default]
        when src is local and dst is s3 - upload=True, download=False
        when src is s3 and dsr is local - upload=False, download=True

        '''
        dst = dst.rstrip("/")
        if upload == False and src.startswith("/"):
            src = src[1:]
        if download == False and dst.startswith("/"):
            dst = dst[1:]

        if all([upload, download]):
            raise Exception("Both upload and download cannot be set as true")

        elif not any([upload, download]):
            '''Condition check - Src directory exists in s3 and both src and dst should not be directory'''
            if not self.os.path.exists(src):
                raise Exception("src (%s) does not exists in s3" % ("/" + src))
            if self.os.path.isdir("/" + src):
                raise Exception("src (%s) cannot be a directory" % ("/" + src))
            if self.os.path.isdir("/" + dst):
                raise Exception("dst (%s) cannot be a directory" % ("/" + dst))
            self.s3_r.Object(self.bucketname, dst).copy_from(CopySource=self.bucketname + "/" + src)

        elif download:
            if not self.os.path.exists(src):
                raise Exception("src (%s) does not exists in s3" % ("/" + src))
            if self.os.path.isdir("/" + src):
                raise Exception("src (%s) cannot be a directory" % ("/" + src))
            if base_os.path.isdir(dst):
                raise Exception("dst (%s) cannot be a directory" % (dst))
            self.s3_c.download_file(self.bucketname, src, dst)

        elif upload:
            if not base_os.path.exists(src):
                raise Exception("src (%s) does not exists in local" % (src))
            if base_os.path.isdir(src):
                raise Exception("src (%s) cannot be a directory" % (src))
            if self.os.path.isdir("/" + dst):
                raise Exception("dst (%s) cannot be a directory" % ("/" + dst))
            self.s3_c.upload_file(src, self.bucketname, dst)

    def copytree(self):
        raise Exception("Not implemented in this version")

    def rmtree(self, x):
        '''
        Remove directory tree s3.

        Restrictions
        ============
        x - dir only
        '''
        x = x.lstrip("/")
        if not self.os.path.exists(x):
            raise Exception("(%s) does not exists in s3" % (x))
        if not self.os.path.isdir(x):
            raise Exception("%s is not a directory" % (x))

        for bucket_object in self.bucket.objects.filter(Prefix=x):
            # Filtering the keys for immediate directories
            self.s3_r.Object(self.bucketname, bucket_object.key).delete()
        
    def move(self, src, dst, upload=False, download=False):
        '''
        move files from src to dst.

        Restrictions
        ============
        1. src - file only
        2. dst - file or directory

        Below options are availaible
        ============================
        when both src and dst are s3    - upload=False, download=False [Default]
        when src is local and dst is s3 - upload=True, download=False
        when src is s3 and dsr is local - upload=False, download=True
        '''
        if upload is False and src.startswith("/"):
            src = src[1:]
        if download == False and dst.startswith("/"):
            dst = dst[1:]

        if all([upload, download]):
            raise Exception("Both upload and download cannot be set as true")

        elif not any([upload, download]):
            if not self.os.path.exists(src):
                raise Exception("src (%s) does not exists in s3" % ("/" + src))
            if self.os.path.isdir("/" + src):
                raise Exception("src (%s) cannot be a directory" % ("/" + src))
            if self.os.path.isdir("/" + dst):
                dst = dst.rstrip("/") + "/" + self.os.path.basename(src)
            self.s3_r.Object(self.bucketname, dst).copy_from(CopySource=self.bucketname+"/"+src)
            self.s3_r.Object(self.bucketname, src).delete()

        elif download:
            if not self.os.path.exists(src):
                raise Exception("src (%s) does not exists in s3" % ("/" + src))
            if self.os.path.isdir("/" + src):
                raise Exception("src (%s) cannot be a directory" % ("/" + src))
            if base_os.path.isdir(dst):
                dst = dst.rstrip("/") + "/" + self.os.path.basename(src)
            self.s3_c.download_file(self.bucketname, src, dst)
            self.s3_r.Object(self.bucketname, src).delete()

        elif upload:
            if not base_os.path.exists(src):
                raise Exception("src (%s) does not exists in local" % (src))
            if base_os.path.isdir(src):
                raise Exception("src (%s) cannot be a directory" % (src))
            if self.os.path.isdir("/" + dst):
                dst = dst.rstrip("/") + "/" + self.os.path.basename(src)
            self.s3_c.upload_file(src, self.bucketname, dst)
            base_os.remove(src)
        
    def make_archive(self):
        raise Exception("Not implemented in this version")

