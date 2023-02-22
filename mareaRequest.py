import requests
import json

class mareaRequest:
    url=""
    date=""
    
    def __init__(self,url,date):
        self.url = url
        self.date = date
        
    def request(self):
        req = requests.get(self.url)
        response = json.loads(req.text)
        return response ["mareas"] ["datos"] ["marea"]