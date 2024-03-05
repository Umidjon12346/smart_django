import json
import requests
from tinydb import TinyDB
from datetime import date
import random

def send_data(data):
    url= 'http://127.0.0.1:8000/api/add/'
    a = requests.post(url=url,json=data)
    return a.status_code

with open('db.json',"r") as file:
    data = json.load(file)

apple = data["Vivo"]
yil = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
a = random.choice(yil)
# oy = [1,2,3,4,5,6,7,8,9,10,11,12]
# v = random.choice(oy)
# kun = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# b = random.choice(kun)
dat = a

for i,v in apple.items():
    item ={
        "price": float(v['price']),
        "img_url": v['img_url'],
        "color": v['color'],
        "ram": int(v["RAM"][0]),
        "memory":int(v['memory'][0:2]),
        "name":v['name'],
        "model":v['company'],
        "release_date": dat
    }
    print(send_data(item))
