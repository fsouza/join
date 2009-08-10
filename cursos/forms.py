#coding:utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from models import Aluno
from util.validacoes import validar_cpf

class CPFField(forms.CharField):
    def clean(self, value):
        if not value:
            raise forms.ValidationError('Este campo é obrigatório.')
        cpf = value.replace('.', '').replace('-', '')
        if not validar_cpf(cpf):
            raise forms.ValidationError('Você deve digitar um CPF válido.')

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    cpf = CPFField(max_length = 15, widget = forms.TextInput())
    password = forms.CharField(max_length = 16, min_length = 4, widget = forms.PasswordInput, label = 'Senha')
    confirmacao_senha = forms.CharField(max_length = 16, min_length = 4, widget = forms.PasswordInput)

    def clean_username(self):
        if User.objects.filter(username = self.cleaned_data['username']).count() > 0:
            raise forms.ValidationError('Já existe um usuário com este login.')

        return self.cleaned_data['username']

    def clean_email(self):
        if User.objects.filter(email = self.cleaned_data['email']).count() > 0:
            raise forms.ValidationError('Já existe um usuário com este e-mail.')

        return self.cleaned_data['email']

    def clean_confirmacao_senha(self):
        if self.cleaned_data['confirmacao_senha'] != self.data['password']:
            raise forms.ValidationError('A senha e a confirmação da senha não correspondem.')

        return self.cleaned_data['confirmacao_senha']

    def save(self, commit = True):
        aluno = super(AlunoForm, self).save(commit = False)
        aluno.set_password(self.cleaned_data['password'])

        if commit:
            aluno.save()

        return aluno
