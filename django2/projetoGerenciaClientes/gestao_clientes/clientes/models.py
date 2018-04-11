from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=75)
    senha = models.CharField(max_length=25)
    email = models.CharField(max_length=75)

    def __str__(self):
        return self.nome

class Scrapy(models.Model):
    pass
