# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    User._meta.get_field('email').blank = False #define o campo email como obrigatório
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']#define quais campos do formulário será usado
        widgets = {#define as características de cada campo
            'first_name': forms.TextInput(attrs={'class':'form-control','maxlength':255, 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','maxlength':255, 'placeholder':'Last Name'}),
            'email': forms.TextInput(attrs={'class':'form-control','maxlength':255, 'placeholder':'E-mail'}),
            'username': forms.TextInput(attrs={'class':'form-control','maxlength':255, 'placeholder':'Username'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','maxlength':255, 'placeholder':'Password'}),
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
            }
        }
    def save(self, commit=True):
        user = super(UserModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
