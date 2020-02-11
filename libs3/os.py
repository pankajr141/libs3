import boto3
from libs3 import path

class OS():
    def __init__(self):
        self.path = path.Path(self)

    def authorize(self, bucketname, aws_access_key_id=None, aws_secret_access_key=None):
        self.s3_r = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.s3_c = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.bucketname = bucketname
        self.bucket = self.s3_r.Bucket(bucketname)

    def listdir(self, directory, filesonly=False):        
        def _listdir(x, filesonly=False):
            '''
            Function will list all the files and folders present in given directory key. 

            filesonly=False  : When set False will work like os.listdir() and yeild all the files and folders,
                               since s3 doesn't have a folder structure we have iterate over all the filtered 
                               keys and filter them ourself.


            filesonly=True  : When set True it will only return files, since it doesn't have to traverse all 
                              the keys its extremely fast
            '''
            if x.startswith("\\") or x.startswith("/"):
                x = x[1:]

            x = x.rstrip("/") + "/"

            # Dealing with edge case scenarios, root directory
            if x == "/":
              x = ""

            if x and not self.path.exists(x):
                raise Exception("%s not exists" % ("/" + x))
            if filesonly:
                for bucket_object in self.bucket.objects.filter(Prefix=x, Delimiter='/'):
                    yield "/" + bucket_object.key.lstrip("/")
                return

            directories_found = []
            for bucket_object in self.bucket.objects.filter(Prefix=x):
                # Filtering the keys for immediate directories
                if bucket_object.key.count("/") == x.count("/") + 1:
                    index = bucket_object.key.index("/", len(x))
                    directories_found.append(bucket_object.key[:index])
                    continue
                if bucket_object.key.count("/") == x.count("/"):
                    yield "/" + bucket_object.key.lstrip("/") 

            # Returning the directories found
            for directory in sorted(list(set(directories_found))):
                yield "/" +  directory.lstrip("/") 
    
        return list(_listdir(directory, filesonly))

    def walk(self):
        raise Exception("Not implemented in this version")

    def mkdir(self, x):
        '''Create directory, throws exception if parent directory not exists'''
        x = x.strip("/")
        if self.path.exists("/" + x):
            raise Exception("%s already exists in s3" % ("/" + x))
        if not self.path.exists(self.path.dirname("/" + x)):
            raise Exception("Parent dir not exist: " + "/" + self.path.dirname(x))

        self.s3_c.put_object(Bucket=self.bucketname, Key=(x + '/'))
    
    def makedirs(self, x):
        '''Create directory, throws exception if parent directory not exists'''
        x = x.strip("/")
        if self.path.exists("/" + x):
            raise Exception("%s already exists in s3" % ("/" + x))

        self.s3_c.put_object(Bucket=self.bucketname, Key=(x + '/'))

    def scandir(self):
        raise Exception("Not implemented in this version")

    def remove(self, x):
        ''' Remove files from s3 '''
        x = x.lstrip("/")
        if not self.path.exists(x):
            raise Exception("(%s) does not exists in s3" % ("/" + x))
        if not self.path.isfile(x):
            raise FileNotFoundError("%s is not a file" % ("/" + x))

        self.s3_r.Object(self.bucketname, x).delete()

    def rmdir(self):
        raise Exception("Not implemented in this version")
        
    def unlink(self):
        raise Exception("Not implemented in this version")
