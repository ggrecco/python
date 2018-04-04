from django.forms import ModelForm
from django import forms
from django.cotrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']#define quais campos do formulário será usado
        widgets = {#define as características de cada campo
            'first_name': forms.TextInput(attrs={'class':'form-control','maxlength':255}),
            'last_name': forms.TextInput(attrs={'class':'form-control','maxlength':255}),
            'email': forms.TextInput(attrs={'class':'form-control','maxlength':255}),
            'username': forms.TextInput(attrs={'class':'form-control','maxlength':255}),
            'password': forms.PasswordInput(attrs={'class':'form-control','maxlength':255}),
        }
        erro_messages = {
            'first_name':{
                'required': 'Este campo é obrigatório'
            },
            'last_name':{
                'required': 'Este campo é obrigatório'
            },
            'email':{
                'required': 'Escreva um e-mail válido'
            },
            'username':{
                'required': 'Este campo é obrigatório'
            },
            'password':{
                'required': 'Este campo é obrigatório'
            }
        }
