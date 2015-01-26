from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
    context_dict = {'boldmessage':"I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)

def about(request): 
    context_dict = {'about_message':"This tutorial has been put together by Akos Szente, 2094613s"}
    return render(request, 'rango/about.html', context_dict)
