"""Define padrões de URL para learning_logs."""
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #pagina inicial
    path('', views.index, name='index'),
    #Mostra todos os assuntos
    path('topics/', views.topics, name='topics'),
    path('new_topic', views.new_topic, name='new_topic'),
    #adicionar uma nova entrada
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry')

]
