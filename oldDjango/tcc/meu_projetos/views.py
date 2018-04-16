from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Servidor, Entrada
from .forms import ServidorForm, EntradaForm
from meu_projetos.scraping import scrapy


def index(request):
    return render(request, 'meu_projetos/index.html')

@login_required
def servidores(request):
    servidores = Servidor.objects.filter(owner=request.user).order_by('id')
    context = {'servidores':servidores}
    return render(request, 'meu_projetos/servidores.html', context )

'''@login_required
def scrapy(request, servidor_id):
    servidor = Servidor.objects.get(id=servidor_id)
    scr = str(servidor.entrada_set.get(id=servidor_id).produto)
    print(scr)
    scrapyt(scr)
    context = {'scr':scr}
    return render(request, 'meu_projetos/scrapy.html', context)'''

@login_required
def servidor(request, servidor_id):
    servidor = Servidor.objects.get(id=servidor_id)
    entradas = servidor.entrada_set.all()
    if servidor.owner != request.user:
        raise Http404
    # entradas = servidor.entrada_set.order_by('-id')
    context = {'servidor':servidor, 'entradas':entradas}
    return render(request, 'meu_projetos/servidor.html', context)

@login_required
def novo_servidor(request):
    if request.method != 'POST':
        form = ServidorForm()
    else:
        form = ServidorForm(request.POST)
        if form.is_valid():
            novo_servidor = form.save(commit=False)
            novo_servidor.owner = request.user
            novo_servidor.save()
            #pegar o nome do servidor e realiza scrapy
            s = Servidor.objects.all()
            scrapy(nome)
            return HttpResponseRedirect(reverse('meu_projetos:servidores'))
    context = {'form':form}
    return render(request, 'meu_projetos/novo_servidor.html', context)
