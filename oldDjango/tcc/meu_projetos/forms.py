from django import forms
from .models import Servidor, Entrada

class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = ['nome']
        labels = {'nome' : ''}
