import os as base_os

class Path():
    def __init__(self, os_obj):
        self.os_obj = os_obj
    
    def exists(self, x):
        '''
        Returns True if passed arguments is dir else False
        Function checks if any key contains the passed argument and return the result.
        '''
        if x.startswith("\\") or x.startswith("/"):
            x = x[1:]
        x = x.rstrip("/")
        for bucket_object in self.os_obj.bucket.objects.filter(Prefix=x):
            if (x in bucket_object.key) and (bucket_object.key.replace(x, '') == "" or bucket_object.key.replace(x, '')[0] == "/"):
                return True
        return False

    def dirname(self, x):
        return base_os.path.dirname(x)
        
    def basename(self, x):
        return base_os.path.basename(x)

    def isdir(self, x):
        '''
        Returns True if passed arguments is dir else False
        Function checks if any key contains the passed argument and return the result.
        '''
        if x.startswith("\\") or x.startswith("/"):
            x = x[1:]
        # Adding in last we make sure that only directory get matched
        x = x.rstrip("/") + "/"

        # Dealing with edge case scenarios, root directory
        if x == "/":
            x = ""

        for bucket_object in self.os_obj.bucket.objects.filter(Prefix=x):
            if (x in bucket_object.key):
                return True
        return False
    
    def isfile(self, x):
        '''
        Returns True if passed arguments is dir else False
        Function checks if any key contains the passed argument and return the result.
        '''
        if x.startswith("\\") or x.startswith("/"):
            x = x[1:]

        x = x.rstrip("/")

        for bucket_object in self.os_obj.bucket.objects.filter(Prefix=x, Delimiter='/'):
            if (x == bucket_object.key):
                return True
        return False