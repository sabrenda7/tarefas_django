from django import forms
from .models import Projeto, Tarefa

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao']


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'data_entrega']
        widgets = {'data_entrega': forms.DateInput(attrs={'type': 'date'}),
        }
