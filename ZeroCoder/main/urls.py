from django.db.backends.utils import names_digest
from django.urls import path
from .import views
# 2 обработка перехода на главную страницу
urlpatterns = [
    path('', views.index, name='home'),    # при переходе на главную страницу запускается функция index из файла views
    path('new', views.new, name='page2')   # прописываем еще один путь для перехода на страницу new
]