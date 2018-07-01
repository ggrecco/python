from django.conf.urls import url
from django.contrib import admin
from todo.core import views


urlpatterns = [
    url(r'', views.home),
    url(r'^admin/', admin.site.urls),
]
