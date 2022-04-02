from django.http import HttpResponse
from django.shortcuts import render
from . models import Post


def post(request):
    # message ='We are a having a test session in Django'
    # return HttpResponse('We are a having a test session in Django')
    # return render(request, 'myblog/index.html', {'message':message})
    return render(request, 'index.html',{})
