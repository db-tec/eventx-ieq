from django import forms
from .models import Evento, Inscricao

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'data_inicial', 'data_final', 'local']

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome', 'sobrenome', 'telefone', 'email', 'evento']