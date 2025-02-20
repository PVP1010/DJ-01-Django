# 1 Самый первый файл который запускается при запуске проекта

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),   # при переходе по адресу /admin/ - открывается приложение (панель) администрвтора
    path('', include('main.urls')),    # переход на главную страницу потом переходим в файл  main.urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
