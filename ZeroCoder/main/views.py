# views.py: файл для отображения HTML-шаблонов. При получении URL-адреса произойдет переход на какую-либо HTML-страницу.

from django.shortcuts import render
from django.http import HttpResponse
# 3 на главной странице будет выводится данный текст
def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница мого проекта на Django</h1>")