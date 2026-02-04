# Mini sistema de gerenciamento de projetos e tarefas

Mini sistema desenvolvido em **Django** para gerenciamento de projetos e tarefas vinculadas a cada projeto.

---

## Funcionalidades
- Cadastro de projetos  
- Cadastro de tarefas vinculadas a um projeto  
- Atualização do status da tarefa (concluída ou não)

---

## Tecnologias utilizadas
- Python  
- Django  
- Django Forms  
- HTML  
- Bootstrap  

---

## Como executar o projeto no windows

### 1 Clone o repositório

```bash
git clone https://github.com/sabrenda7/tarefas_django.git
cd tarefas_django
```

### 2 Crie e ative o ambiente virtual

```bash
python -m venv .venv
```

### 3 Ative o ambiente virtual
```bash
.venv\Scripts\activate
```

### 4 Instale 

```bash
pip install django
```

### 5 Inicie o servidor

```bash
python manage.py migrate
python manage.py runserver
```

###6 Acesse no navegador
http://127.0.0.1:8000/projetos/


