from django.http import HttpResponse
from django.shortcuts import render
import datetime


def adminPage(request,name):
    return HttpResponse('Hi, ' + name + ' admin')


def yearPage(request,year):
    if 1000 <= year <= 9999:
        return HttpResponse(f"Year is {year}")
    else:
        return HttpResponse("Year must be a four-digit number", status=404)

def index(request):
    timezone = datetime.timezone(datetime.timedelta(hours=8))
    data = {'dt':datetime.datetime.now(tz = timezone),
            'dz':timezone
            
            }
    return render(request, 'index.html', data)


""""

def index(request):
    dt = datetime.now()
    return render(request, 'index.html', locals())

"""