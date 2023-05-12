import aiohttp
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render
import requests
from django.core.cache import caches

redis_cache = caches["default"]

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def api(request: HttpRequest) -> JsonResponse:
    data = redis_cache.get('api')
    if data is None:
        data = requests.get("http://127.0.0.1:8003/api").json()
        redis_cache.set('api', data, timeout=10)
    print(data)
    return JsonResponse(data=data, safe=False)
    # async with aiohttp.ClientSession() as session:
    #     async with session.get("http://127.0.0.1:8003/api") as response:
    #         data = await response.json()
    #         print(data)
    #         return data
