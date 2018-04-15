from django.db import models
from django.contrib.auth.models import User

class Servidor(models.Model):
    nome = models.CharField(max_length=100)
    produto = models.CharField(max_length=50)
    cveid = models.CharField(max_length=50)
    tipo = models.CharField(max_length=200)
    dataCorrecao = models.CharField(max_length=50)
    nota = models.CharField(max_length=10)
    tipoAcesso = models.CharField(max_length=200)
    comentario = models.TextField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.nome

class Entrada(models.Model):
    servidor = models.ForeignKey(Servidor)
    obs = models.ForeignKey(User)


    class Meta:
        verbose_name_plural = 'entradas'

    def __str__(self):
        return self.obs[:50] + "..."



'''from django.db import models
from django.contrib.auth.models import User

class Servidor(models.Model):
    nome = models.CharField(max_length=100)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.nome

class Entrada(models.Model):
    servidor = models.ForeignKey(Servidor)
    produto = models.CharField(max_length=50)
    cveid = models.CharField(max_length=50)
    tipo = models.CharField(max_length=200)
    dataCorrecao = models.CharField(max_length=50)
    nota = models.CharField(max_length=10)
    tipoAcesso = models.CharField(max_length=200)
    comentario = models.TextField()

    class Meta:
        verbose_name_plural = 'entradas'

    def __str__(self):
        return self.produto+ " - " +self.comentario[:50] + "..."
'''
