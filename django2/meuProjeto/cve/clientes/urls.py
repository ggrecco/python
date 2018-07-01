from django.urls import path
from .views import listar_cliente, cadastrar_cliente, atualizar_cliente, excluir_cliente

urlpatterns = [
    path('listar/', listar_cliente, name='listar_cliente'),
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('atualizar/<int:id>/', atualizar_cliente, name='atualizar_cliente'),
    path('excluir/<int:id>/', excluir_cliente, name='excluir_cliente'),
]
