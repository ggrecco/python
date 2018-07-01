from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('meu_projetos.urls', namespace='meu_projetos')),
    url(r'^users/', include('users.urls', namespace='users')),
]
