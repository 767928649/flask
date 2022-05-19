# -*- coding: utf-8 -*-
# @Time    : 2022/5/18 下午9:07
# @Author  : Ly
import db
from flask import Blueprint
from flask import Flask, render_template, request, redirect, session, jsonify

blueprint = Blueprint('todos', __name__, url_prefix='/todos')


@blueprint.route('/add', methods=['POST'])
def addTodo():
    userid = session.get('userId')
    status = 'todo'
    title = request.json['title']
    t = db.addTodos(userId=userid, status=status, title=title)
    if t:
        return jsonify({'code': 200, 'message': '添加成功'})
    return jsonify({'code': 400, 'message': '添加失败'})


@blueprint.route('/delete', methods=['POST'])
def deleteTodo():
    todoId = request.json['todoId']
    t = db.deleteTodo(todoId=todoId)
    if t:
        return jsonify({'code': 200, 'message': '删除成功'})
    return jsonify({'code': 400, 'message': '删除失败'})



