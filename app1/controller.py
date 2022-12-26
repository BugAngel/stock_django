from django.http import JsonResponse
from app1.start_star import startStar
from django.core import serializers

# Create your views here.
def index(request):
    return JsonResponse("123", safe=False)

def startStarController(request):
    # TODO 完成次N日收盘价关联功能
    if request.method == 'GET':
        firstDate = request.GET.get('firstDate')
        secondDate = request.GET.get('secondDate')
        thirdDate = request.GET.get('thirdDate')
        return JsonResponse(serializers.serialize("json",startStar(firstDate, secondDate, thirdDate)), safe=False)
    return '{}'
