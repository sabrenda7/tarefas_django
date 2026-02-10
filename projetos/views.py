from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/lista_projetos.html', {
        'projetos': projetos
    })

def novo_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()

    return render(request, 'projetos/novo_projeto.html', {
        'form': form
    })

def lista_tarefas(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    tarefas = projeto.tarefas.all()

    return render(request, 'projetos/lista_tarefas.html', {
        'projeto': projeto,
        'tarefas': tarefas
    })

def nova_tarefa(request, id):
    projeto = get_object_or_404(Projeto, id=id)

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.projeto = projeto
            tarefa.save()
            return redirect('lista_tarefas', id=projeto.id)
    else:
        form = TarefaForm()

    return render(request, 'projetos/nova_tarefa.html', {
        'form': form,
        'projeto': projeto
    })

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if tarefa.status == 'P':
        tarefa.status = 'E'
    elif tarefa.status == 'E':
        tarefa.status = 'C'
    else:
        tarefa.status = 'P'

    tarefa.save()

    return redirect('lista_tarefas', tarefa.projeto.id)
