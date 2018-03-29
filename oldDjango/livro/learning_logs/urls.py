"""Define padrões de URL para learning_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    #lista assunto
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #Adiciona assuntos
    url(r'^new_topics/$', views.new_topic, name='new_topic'),
    #Página Para adicionar uma nova entrada
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]
