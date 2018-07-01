from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

def listar_cliente(request):
    clientes = Cliente.objects.all()
    return  render(request, 'lista_cliente.html', {'clientes': clientes})

def cadastrar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_cliente')
    return render(request, 'formulario_cliente.html', {'form' : form})

def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listar_cliente')
    return render(request, 'formulario_cliente.html', {'form':form})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('listar_cliente')
    return render(request, 'conf_deletar_cliente.html', {'cliente':cliente})
