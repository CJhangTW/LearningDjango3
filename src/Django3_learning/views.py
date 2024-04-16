from django.http import HttpResponse
from django.shortcuts import render


def adminPage(request,name):
    return HttpResponse('Hi, ' + name + ' admin')


def yearPage(request,year):
    if 1000 <= year <= 9999:
        return HttpResponse(f"Year is {year}")
    else:
        return HttpResponse("Year must be a four-digit number", status=404)

def index(request):
    return render(request, 'index.html')