from django.urls import path
from .import views
# 2 обработка перехода на главную страницу
urlpatterns = [
    path('', views.index)    # при переходе на главную страницу запускается функция index из файла views
]