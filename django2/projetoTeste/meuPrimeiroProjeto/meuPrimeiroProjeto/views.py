from django.http import HttpResponse

def hello(request):
    return HttpResponse('Ola Mundo')

def articles(request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))
