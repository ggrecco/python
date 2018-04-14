from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Servidor
from .forms import ServidorForm

def index(request):
    return render(request, 'meu_projetos/index.html')

def servidores(request):
    servidores = Servidor.objects.order_by('id')
    context = {'servidores':servidores}
    return render(request, 'meu_projetos/servidores.html', context )

def servidor(request, servidor_id):
    servidor = Servidor.objects.get(id=servidor_id)
    entradas = servidor.entrada_set.order_by('-id')
    context = {'servidor':servidor, 'entradas':entradas}
    return render(request, 'meu_projetos/servidor.html', context)

def novo_servidor(request):
    if request.method != 'POST':
        form = ServidorForm()
    else:
        form = ServidorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('meu_projetos:servidores'))
    context = {'form':form}
    return render(request, 'meu_projetos/novo_servidor.html', context)
'''
def novo_entrada(request, servidor_id):
    servidor = Servidor.objects.get(id=servidor_id)
    if request.method != 'POST':
        form = EntradaForm()
    else:
        form = EntradaForm(data=request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.servidor = servidor
            nova_entrada.save()
            return HttpResponseRedirect(reverse('meu_projetos:servidor', args=[servidor_id]))
    context = {'servidor' : servidor, 'form' : form}
    return render(request, 'meu_projetos/nova_entrada.html', context)
'''
