#coding:utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from models import Aluno, Curso
from util.validacoes import validar_cpf

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    cpf = forms.CharField(max_length = 15, widget = forms.TextInput())
    password = forms.CharField(max_length = 16, min_length = 4, widget = forms.PasswordInput, label = 'Senha')
    confirmacao_senha = forms.CharField(max_length = 16, min_length = 4, widget = forms.PasswordInput)
    email = forms.EmailField(max_length = 200, min_length = 6, label = 'E-mail', required = True)
    first_name = forms.CharField(max_length = 50, min_length = 3, required = True)
    last_name = forms.CharField(max_length = 100, min_length = 3, required = True)

    def clean_cpf(self):
        self.cleaned_data['cpf'] = self.cleaned_data['cpf'].replace('.', '').replace('-', '')
        if not validar_cpf(self.cleaned_data['cpf']):
            raise forms.ValidationError('Você deve digitar um CPF válido.')

        if Aluno.objects.filter(cpf = self.cleaned_data['cpf']).count() > 0:
            raise forms.ValidationError('Este CPF já está cadastrado.')

        return self.cleaned_data['cpf']

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
        aluno.cpf = self.cleaned_data['cpf']

        if commit:
            aluno.save()

        return aluno
