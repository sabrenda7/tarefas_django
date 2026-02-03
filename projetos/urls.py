from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/novo/', views.novo_projeto, name='novo_projeto'),
    path('projetos/<int:id>/tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('projetos/<int:id>/tarefas/nova/', views.nova_tarefa, name='nova_tarefa'),
    path('tarefas/<int:id>/editar/', views.editar_tarefa, name='editar_tarefa'),
]
