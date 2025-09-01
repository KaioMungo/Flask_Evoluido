# FlaskEvoluido

Aplicação web simples em Flask para gerenciar usuários e tarefas, utilizando SQLAlchemy para ORM e SQLite como banco de dados.

---

## Funcionalidades

- CRUD completo para **Usuários** (criar, listar, atualizar, deletar)
- CRUD completo para **Tarefas** associadas a usuários
- Relacionamento entre usuários e tarefas (um usuário pode ter várias tarefas)
- Interface web simples com templates HTML usando Jinja2

---

## Tecnologias utilizadas

- Python 3.11
- Flask
- Flask-SQLAlchemy
- SQLite (banco de dados)
- Jinja2 (templates HTML)

---

## Como rodar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/KaioMungo/FlaskEvoluido.git
cd FlaskEvoluido

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
pip install -r requirements.txt
python app.py

