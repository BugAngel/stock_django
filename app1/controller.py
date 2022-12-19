from django.shortcuts import render
from django.http import JsonResponse
from app1.start_star import startStar
from django.core import serializers

# Create your views here.
def index(request):
    return JsonResponse("123", safe=False)

def startStarController(request,firstDate, secondDate, thirdDate):
    return JsonResponse(serializers.serialize("json",startStar(firstDate, secondDate, thirdDate)), safe=False)
