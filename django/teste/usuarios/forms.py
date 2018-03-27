#-*- coding:utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class userModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password'] #define os campos que serão utilizados
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','maxlenght':255}),
            'last_name':forms.TextInput(attrs={'class':'form-control','maxlenght':255}),
            'email':forms.TextInput(attrs={'class':'form-control','maxlenght':255}),
            'username':forms.TextInput(attrs={'class':'form-control','maxlenght':255}),
            'password':forms.PasswordInput(attrs={'class':'form-control','maxlenght':255}),
        }

        error_messages = {
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
            },
        }
