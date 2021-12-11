import requests
import json

class file:
    def __init__(self, title, content, language=""):
        self.title = title
        self.content = content
        self.language = language

class responce:
    def __init__(self, j):
        self.__dict__.update(**json.loads(j))

class manager:
    def __init__(self,token):
        self.url = "https://api.github.com/gists"
        self.token = token
    def create(self,files,desc="",ispublic=False):
        filenames = {}
        for i in files:filenames.update(
        {i.title:{'content':i.content,'laungage':i.language}})
        payload = {"description":desc,"public":False,"files":filenames}
        return responce(requests.post(self.url,
        headers={'Authorization':'token '+self.token},
        params={'scope':'gist'},data=json.dumps(payload)).text)
    def get(self,id):
        return responce(requests.get(f'{self.url}/{id}',
        headers={'Authorization':'token '+self.token}).text)
    def update(self,id,files,desc=""):
        filenames = {}
        for i in files:filenames.update({i.title:
        {'content':i.content,'laungage':i.language}})
        return responce(requests.post(f'{self.url}/{id}',
        headers={'Authorization':'token '+self.token},
        data=json.dumps({"description":desc,"files":filenames})).text)
    def delete(self,id):
        responce(requests.delete(f'{self.url}/{id}',
        headers={'Authorization':'token '+self.token}).text)
