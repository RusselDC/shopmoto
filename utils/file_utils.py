import json

class FileUtils:
    
    def read_file(self):
        file = open("./creds/db_cred.json")
        result = file.read()
        file.close()
        return result