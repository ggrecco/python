from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #Mostra os servidores
    url(r'^servidores/$', views.servidores, name='servidores'),
    url(r'^servidores/(?P<servidor_id>\d+)/$', views.servidor, name='servidor' ),
    url(r'^novo_servidor/$', views.novo_servidor, name='novo_servidor' ),
    url(r'^scrapy/(?P<scrapy_id>\d+)$', views.scrapy, name='scrapy' ),#teste para adicionar funções diferentes na mesma URL
    # url(r'^nova_entrada/(?P<servidor_id>\d+)/$', views.nova_entrada, name='nova_entrada'),
]
