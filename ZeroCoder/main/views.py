# views.py: файл для отображения HTML-шаблонов. При получении URL-адреса произойдет переход на какую-либо HTML-страницу.

from django.shortcuts import render
from django.http import HttpResponse
# 3 на главной странице будет выводится данный текст

def index(request):
    data= {
        "caption": "DjangoCosmos"
    }
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')
