from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(requests):
    data={"test":"000"}
    return JsonResponse(data)