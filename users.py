# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 下午9:07
# @Author  : Ly
import db
from flask import Blueprint
from form import LoginForm, RegisterForm
from flask import Flask, render_template, request, redirect, session

blueprint = Blueprint('users', __name__, url_prefix='/users')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # 判断登录请求是否为 post,不是 post 请求直接渲染返回登录页面
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        form = LoginForm()
        # 第一步验证表单字段是否合法
        if form.validate_on_submit():
            # 第二步获取,表单中 name 和 pwd 到数据库中验证.
            name = form.name.data
            pwd = form.password.data
            user = db.login(name, pwd)
            # 如果用户验证成功,则登录成功,session 设置为 True,并设置 userId 为登录 userId 重定向到首页/
            if user:
                session['hasLogin'] = True
                session['userId'] = user.userId
                return redirect('/')
        return render_template('login.html', form=form)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = RegisterForm()
        if form.validate_on_submit():
            name = form.name.data
            pwd = form.password.data
            if db.register(name, pwd):
                return redirect('/')
        return render_template('register.html', form=form)
    else:
        form = RegisterForm()
        return render_template('register.html', form=form)


@blueprint.route('/logout')
def logout():
    session['hasLogin'] = False
    return redirect('/')


