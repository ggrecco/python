from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))


def lerDobanco(nome):
    lista_nomes = [
        {'nome': 'Karim', 'idade':'35'},
        {'nome': 'Gustavo', 'idade':'32'},
        {'nome': 'Darth', 'idade':'1'},
        {'nome': 'Vader', 'idade':'1'}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome':'', 'idade':'0'}

def fname(request, nome):
    result = lerDobanco(nome)
    # print(result)
    if result['idade'] != '0':
        return HttpResponse('A pessoa '+ result['nome'] +' encontrada tem ' + result['idade'] + ' anos.')
    else:
        return HttpResponse('Pessoa não encontrada')

def fname2(request, nome):
    idade = lerDobanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})
