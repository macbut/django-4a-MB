from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world")

def counter(request):
    text_fills = open("./templates/counter.html")
    page = text_fills.read()
    text_fills.close()
    return HttpResponse(page)

def basic(request):
    text_fills = open("./templates/basic.html")
    page = text_fills.read()
    text_fills.close()
    return HttpResponse(page)