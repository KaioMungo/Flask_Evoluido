import os
from flask import Flask
from config import Config # importa as 
from controllers.user_controller import UserController
from controllers.task_controller import TaskController
from database import db

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)

# inicializa o banco de dados
db.init_app(app)

# cria tabelas

with app.app_context():
    db.create_all()

# forma alternativa de criar rotas, parâmetros: rota em si, endpoint interno do flask e função a ser executada quando a URL for acessada


#----------------------------------------user--------------------------------------------------------#
app.add_url_rule('/users', view_func=UserController.list_users, methods=['GET'], endpoint='list_users')
app.add_url_rule('/users/new', view_func=UserController.create_user, methods=['GET', 'POST'], endpoint='create_user')
app.add_url_rule('/users/update/<int:user_id>', view_func=UserController.update_user, methods=['GET', 'POST'], endpoint='update_user')
app.add_url_rule('/users/delete/<int:user_id>', view_func=UserController.delete_user, methods=['POST'], endpoint='delete_user')


#----------------------------------------task--------------------------------------------------------#
app.add_url_rule('/tasks', view_func=TaskController.list_tasks, methods=['GET'], endpoint='list_tasks')
app.add_url_rule('/tasks/new', view_func=TaskController.create_task, methods=['GET', 'POST'], endpoint='create_task')
app.add_url_rule('/tasks/update/<int:task_id>', view_func=TaskController.update_task_status, methods=['POST'], endpoint='update_task_status')
app.add_url_rule('/tasks/delete/<int:task_id>', view_func=TaskController.delete_task, methods=['POST'], endpoint='delete_task')



if __name__ == '__main__':
    app.run(debug=True, port=5002)