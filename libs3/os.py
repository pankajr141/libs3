import boto3
from libs3 import path

class OS():
    def __init__(self):
        self.path = path.Path(self)

    def authorize(self, bucket, aws_access_key_id=None, aws_secret_access_key=None):
        self.s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.bucket = self.s3.Bucket(bucket)

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
                yield "/" + bucket_object.key.lstrip("/") 

            # Returning the directories found
            for directory in list(set(directories_found)):
                yield "/" +  directory.lstrip("/") 
        return list(_listdir(directory, filesonly))

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
