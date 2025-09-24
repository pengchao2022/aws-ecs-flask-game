from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Todo
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
def add():
    content = request.form.get('content')
    if content:
        new_task = Todo(content=content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/update/<int:id>')
def update(id):
    task = Todo.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))