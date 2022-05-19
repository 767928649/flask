# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 下午9:02
# @Author  : Ly
# 数据库访问逻辑
from app import app
from flask_sqlalchemy import SQLAlchemy

user = 'root'
password = 'root'
database = 'todoDB'
uri = 'mysql://%s:%s@localhost:3306/%s' %(user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
orm = SQLAlchemy(app)


class User(orm.Model):
    __tablename__ = 'users'
    userId = orm.Column(orm.Integer, primary_key=True)
    name = orm.Column(orm.String(255))
    password = orm.Column(orm.String(255))


class Todo(orm.Model):
    __tablename__ = 'todos'
    todoId = orm.Column(orm.Integer, primary_key=True)
    userId = orm.Column(orm.Integer)
    status = orm.Column(orm.String(255))
    title = orm.Column(orm.String(255))


# 函数 login 在表 users 中查找与 name、password 匹配的用户，如果存在，则表示登录成功。
def login(name, password):
    users = User.query.fileter_by(name=name, password=password)
    user = users.first()
    return user


# 函数 register 根据 name、password 创建一个新的用户，然后插入到表 users 中。
def register(name, password):
    user = User(name=name, password=password)
    orm.session.add(user)
    orm.session.commit()
    return True


# 函数 getTodos(userId) 在表中查询属于指定用户的待做事项。
def getTodos(userId):
    todos = Todo.query.filter_by(userId)
    return todos


# 函数 addTodo(userId, status, title) 根据 userId、status、title 创建一个新的待做事项，然后插入到表 todos 中。
def addTodos(userId, status, title):
    todo = Todo(userId=userId, status=status, title=title)
    orm.session.add(todo)
    orm.session.commit()
    return True


# 函数 updateTodo(todoId，status) 更新待做事项的 status，当用户完成一个待做事项时，需要将待做事项的 status 从 “todo” 更改为 “done”。
def updateTodo(todoId, status):
    todos = Todo.query.filter_by(todoId=todoId)
    todos.update({'status': status})
    orm.session.commit()
    return True


# 函数 deleteTodo(todoId) 删除待做事项。
def deleteTodo(todoId):
    todos = Todo.query.filter_by(todoId)
    todos.delete()
    orm.session.commit()
    return True
