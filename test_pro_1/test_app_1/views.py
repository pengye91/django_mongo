from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    u = models.TestModel(name = 'pengye', age = 23)
    u.save()
    u_json=str(u.to_mongo())

    return HttpResponse(u_json)
