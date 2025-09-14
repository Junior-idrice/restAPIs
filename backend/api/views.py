from django.shortcuts import render
from django.http import  JsonResponse
# Create your views here.


def home(request):
    headers = request.headers
    get_data = request.GET
    post_data = request.POST

    print(headers)
    print(get_data)
    print(post_data)
    return JsonResponse({'info':'DJANGO REACT COURSE','name':'idrice'})

