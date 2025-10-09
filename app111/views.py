from django.shortcuts import render
from django.http import HttpResponse

def app111_funksiya1(request):
    return HttpResponse("app111 ning 1-funksiyasi ishlamoqda ")

def app111_funksiya2(request):
    return HttpResponse("app111 ning 2-kunksiyasi ishlamoqda ")

def app111_funksiya3(request):
    return HttpResponse("app111 ning 3-kunksiyasi ishlamoqda ")