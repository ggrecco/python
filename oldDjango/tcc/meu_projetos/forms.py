from django import forms
from .models import Servidor

class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = ['nome']
        labels = {'nome' : ''}
