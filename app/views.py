from django.http import HttpResponse
from django.shortcuts import render, reverse
import time
import os

def home_view(request):
    templates_name = 'app/home.html'
    pages = {
        'Главная страница': '',
        'Показать текущее время': 'current_time/',
        'Показать содержимое рабочей директории': 'workdir/'
    }
    context = {
        'pages': pages
    }
    return render(request, templates_name, context)


def time_view(request):
    current_time = time.strftime("%H:%M  %d.%m.%y")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    templates_name = 'app/workdir.html'
    workdir = sorted(os.listdir())
    msg = (f"{work} " for work in workdir)
    return render(request,templates_name, context={'work': workdir})