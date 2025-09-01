from flask import render_template, request, redirect, url_for
from database import db
from models.user import User

class UserController:

    @staticmethod
    def list_users():
        users = User.query.all()
        return render_template('users.html', users=users)

    @staticmethod
    def create_user():
        if request.method == 'GET':
            return render_template('create_user.html')
        elif request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('list_users'))

    @staticmethod
    def update_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return "Usuário não encontrado", 404

        if request.method == 'GET':
            return render_template('update_user.html', user=user)
        elif request.method == 'POST':
            user.name = request.form.get('name')
            user.email = request.form.get('email')
            db.session.commit()
            return redirect(url_for('list_users'))

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return redirect(url_for('list_users'))
