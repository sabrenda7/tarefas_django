from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('E', 'Em andamento'),
        ('C', 'Concluída'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P'
    )

    data_entrega = models.DateField(null=True, blank=True)
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='tarefas'
    )

    def __str__(self):
        return self.titulo

