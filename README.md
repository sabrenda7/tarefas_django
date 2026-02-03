#Mini sistema de gerenciamento de projetos e tarefas

Mini sistema desenvolvido em **Django** para gerenciamento de projetos e tarefas vinculadas a cada projeto.

---

##Funcionalidades
- Cadastro de projetos  
- Cadastro de tarefas vinculadas a um projeto  
- Atualização do status da tarefa (concluída ou não)

---

##Tecnologias utilizadas
- Python  
- Django  
- Django Forms  
- HTML  
- Bootstrap  

---

##Como executar o projeto

###1 Clone o repositório

```bash
git clone https://github.com/sabrenda7/tarefas-django.git
cd tarefas-django
```

###2 Crie e ative o ambiente virtual

```bash
python -m venv .venv
```

# Windows

```bash
.venv\Scripts\activate
```

###3 Instale as dependencias 

```bash
pip install -r requirements.txt
```

###4 Inicie o servidor

```bash
python manage.py migrate
```

###5 Acesse no navegador
http://127.0.0.1:8000/projetos/


