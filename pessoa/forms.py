from django import forms
from .models import PessoaModel

class PessoaForm(forms.ModelForm):
    pessoa_nome = forms.CharField(required=True, label="Nome")
    pessoa_logradouro = forms.CharField(required=True, label="Logradouro")
    pessoa_numero = forms.CharField(required=True, label="Número")

    class Meta:
        model = PessoaModel
        fields = [
            'pessoa_nome',
            'pessoa_logradouro',
            'pessoa_numero'
        ]
