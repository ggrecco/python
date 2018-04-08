from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from clientes import urls as clientes_urls

urlpatterns = [
    path('list/', persons_list),

]
