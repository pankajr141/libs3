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