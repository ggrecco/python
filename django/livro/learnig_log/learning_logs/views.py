from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm
from .models import Topic
from .forms import TopicForm, EntryForm

def index(request):
    """A página inicial de Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def new_topic(request):
    """Adiciona um  novo assunto"""
    if request.method != 'POST':
        #Cria um formulário em branco
        form = TopicForm()
    else:
        #processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto em particular."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        #Nenhum dado submetido; cria um formulario em branco
        form = EntryForm()
    else:
        #Dados de POST submetidos; processa os Dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form' : form}
    return render(request, 'learning_logs/new_entry.html', context)
