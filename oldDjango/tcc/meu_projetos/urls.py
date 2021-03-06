from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #Mostra os servidores
    url(r'^servidores/$', views.servidores, name='servidores'),
    url(r'^servidores/(?P<servidor_id>\d+)/$', views.servidor, name='servidor' ),
    url(r'^novo_servidor/$', views.novo_servidor, name='novo_servidor' ),
]
