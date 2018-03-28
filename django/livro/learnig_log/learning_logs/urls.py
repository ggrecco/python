"""Define padrões de URL para learning_logs."""
from django.urls import path
from . import views

urlpatterns = [
    #pagina inicial
    path('', views.index, name='index'),
    #Mostra todos os assuntos
    path('topics/', views.topics, name='topics'),
]
