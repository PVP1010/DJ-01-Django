from django.shortcuts import render
from django.http import HttpResponse
# 3 на главной странице будет выводится данный текст
def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")