# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 下午9:00
# @Author  : Ly
# flask程序入口
from app import app
# 导入模板使用的函数,和 session
from flask import render_template, session
import db
import users
import todos
# 在 Flask 实例中注册这两个蓝图
app.register_blueprint(users.blueprint)
app.register_blueprint(todos.blueprint)


@app.route('/')
def index():
    hasLogin = session.get('hasLogin')
    if hasLogin:
        userId = session.get('userId')
        itmes = db.getTodos(userId)
        todos = [itmes for item in itmes if item.status == 'todo']
        dones = [itmes for item in itmes if item.status == 'done']
    else:
        items = []
        todos = []
        dones = []
    return render_template('index.html', hasLogin=hasLogin, todos=todos, dones=dones)


app.run()