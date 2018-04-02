from django.db import models

class Topic(models.Model):
    """Assunto que o usuário inseri"""
    produto = models.CharField(max_length=200)
    cveid = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    datacorrecao = models.CharField(max_length=200)
    nota = models.CharField(max_length=200)
    acesso = models.CharField(max_length=200)
    comentários = models.CharField(max_length=200)


    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text
