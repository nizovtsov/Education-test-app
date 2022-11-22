from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello. beginning of a test blog and later moving to test platform!")
