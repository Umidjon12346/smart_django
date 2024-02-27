import json
import requests
from tinydb import TinyDB

def send_data(data):
    url= 'http://127.0.0.1:8000/api/add/'
    a = requests.post(url=url,json=data)
    return a.status_code

with open('db.json',"r") as file:
    data = json.load(file)

apple = data["Samsung"]

for i,v in apple.items():
    item ={
        "price": v['price'],
        "img_url": v['img_url'],
        "color": v['color'],
        "ram": v["RAM"],
        "memory":v['memory'],
        "name":v['name'],
        "model":v['company']
    }
    print(send_data(item))
