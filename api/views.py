from django.http import HttpRequest, JsonResponse
import json
from .models import Smartphones
from datetime import date
import random


def add_product(reqeust: HttpRequest):
    body = reqeust.body.decode("utf-8")
    data = json.loads(body)
    name = data.get("name",False)
    img_url = data.get("img_url",False)
    color = data.get("color",False)
    ram = data.get("ram",False)
    memory = data.get("memory",False)
    price = data.get("price",False)
    model = data.get("model",False)
    
    if price == False:
        return JsonResponse({'status':'price not found'})
    if img_url == False:
        return JsonResponse({'status':'img not found'})
    if color == False:
        return JsonResponse({'status':'color not found'})
    if ram == False:
        return JsonResponse({'status':'ram not found'})
    if memory == False:
        return JsonResponse({'status':'memory not found'})
    if name == False:
        return JsonResponse({'status':' name not found'})
    if model == False:
        return JsonResponse({'status':'model not found'})
    
    yil = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
    a = random.choice(yil)
    # oy = [1,2,3,4,5,6,7,8,9,10,11,12]
    # v = random.choice(oy)
    # kun = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    # b = random.choice(kun)
    # dat = date(year=a,month=v,day=b)
    dat = a
    Smartphones.objects.create(
        price = price,
        img_url = img_url,
        color = color,
        ram = ram,
        memory = memory,
        name = name,
        model = model,
        release_date = dat  
    )
    return JsonResponse(data)

def delete(request,pk):
    smart = Smartphones.objects.get(id=pk)
    smart.delete()
    return JsonResponse({"message": "deleted"}) 

def get_product(reqeust: HttpRequest, pk: int) -> JsonResponse:
    smart = Smartphones.objects.get(id=pk)
    data = {
        "price" : smart.price,
        "img_url" : smart.img_url,
        "color" : smart.color,
        "ram" : smart.ram,
        "memory" : smart .memory,
        "name" : smart.name,
        "model" : smart.model
    }
    return JsonResponse(data)

def get_products(request:HttpRequest):
    smart = Smartphones.objects.all()
    data = [] 
    for i in smart:
        data.append( i.to_dict())
    return JsonResponse(data,safe=False)
def do_updates(request:HttpRequest,pk):
    smart = Smartphones.objects.get(id=pk)
    a = json.loads(request.body.decode("utf-8"))
    smart.price = a.get('price',smart.price)
    smart.img_url= a.get('img_url',smart.img_url)
    smart.color = a.get('color',smart.color)
    smart.ram = a.get("ram",smart.ram)
    smart.memory = a.get("memory",smart.memory)
    smart.name = a.get("name",smart.name)
    smart.model = a.get("model",smart.model)
    smart.release_date = a.get("release_date",smart.release_date)
    smart.save()
    return JsonResponse({"message": "Updated"})

def get_by_name(request:HttpRequest,pk):
    smart = Smartphones.objects.filter(name__contains = pk)
    data = []
    for i in smart:
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)
def get_color(request:HttpRequest,kk):
    smart = Smartphones.objects.filter(color__contains = kk)
    data = []
    for i in smart:
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)
def get_date(request:HttpRequest,pk):
    smart = Smartphones.objects.filter(release_date = pk)
    data = []
    for i in smart:
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)
def get_price(request:HttpRequest,pk,pp):
    smart = Smartphones.objects.filter(price__gte =pk,price__lte = pp)
    data = []
    for i in smart:
        data.append(i.to_dict())
    return JsonResponse(data,safe =False)
def get_endWith(request:HttpRequest,pk):
    smart = Smartphones.objects.filter(name__endswith=pk)
    data = []
    for i in smart:
        data.append(i.to_dict())
    return JsonResponse(data,safe = False)
def get_brend(request:HttpRequest):
    model = Smartphones.objects.all()
    data = []
    for i in model:
        a = i.to_dict()
        if a["model"] not in data:
            data.append(a["model"])
    return JsonResponse(data,safe=False)
def get_by_brend_all(requests:HttpRequest,pk):
    model = Smartphones.objects.filter(model = pk)
    data = []
    for i in model:
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)

    
            