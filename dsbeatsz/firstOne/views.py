from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hello M.F.</h1>')


def test(request):
    return HttpResponse('<h1>Test Page M.F.</h1>')
     
