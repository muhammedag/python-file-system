import os
import json
import requests

class FileSystem():

    def CreateFile(file, content):
        check = os.path.exists(file)
        if check:
            create = open(file, "a")
            write = create.write(content)
            if write:
                return 1
            else:
                return 0
        else:
            create = open(file, "w")
            write = create.write(content)
            if write:
                return 1
            else:
                return 0

    def DeleteFile(file):
        check = os.path.exists(file)
        if check:
            delete = os.remove(file)
            if delete:
                return 0
            else:
                return 1
        else:
            return 0

    def CreateFolder(folder):
        check = os.path.exists(folder)
        if check:
            return 1
        else:
            create = os.mkdir(folder)
            if create:
                return 0
            else:
                return 1

    def DeleteFolder(folder):
        check = os.path.exists(folder)
        if check:
            delete = os.rmdir(folder)
            if delete:
                return 0
            else:
                return 1
        else:
            return 0

    def ListFolder(path = 0):
        if path:
            data = os.listdir(path)
            return data
        else:
            data = os.listdir()
            return data

    def GetFile(file):
        get = open(file, "rb")
        data = get.read()
        return data

    def FileUpload(data):
        url = "https://ipfs.infura.io/ipfs/"
        file = {"content" : data}
        response_hash = requests.post("https://ipfs.infura.io:5001/api/v0/add", files = file)
        request = response_hash.json()
        hash = request["Hash"]
        output = url + hash 
        return output
