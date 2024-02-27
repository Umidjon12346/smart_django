from django.http import HttpRequest, JsonResponse
import json
from .models import Smartphones


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
    
    Smartphones.objects.create(
        price = price,
        img_url = img_url,
        color = color,
        ram = ram,
        memory = memory,
        name = name,
        model = model
    )
    return JsonResponse(data)

def delete(request,pk):
    smart = Smartphones.objects.get(id=pk)
    smart.delete()
    return JsonResponse({"message": "deleted"})

def get_product(reqeust: HttpRequest, pk: int) -> JsonResponse:
    smart = Smartphones.objects.get(id=pk)
    data = {
        "price" : data.price,
        "img_url" : data.img_url,
        "color" : data.color,
        "ram" : data.ram,
        "memory" : data .memory,
        "name" : data.name,
        "model" : data.model
    }
    return JsonResponse(data)

    
    