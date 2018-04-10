from django.db import models

class usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.PasswordField(max_length=200)

    def __str__(self):
        return self.text
