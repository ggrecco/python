from django.shortcuts import render
from usuarios.forms import userModelForm
from django.http import HttpResponse

def cadastro(request):
    from userModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'usuarios/cadastro.html', context)
