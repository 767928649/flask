# -*- coding: utf-8 -*-
# @Time    : 2022/5/19 上午10:52
# @Author  : Ly
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """登录表单"""
    name = StringField(
        label='名字',
        validators=[
            DataRequired(message='名字不能为空')
        ]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=3, message='密码至少包括 3 个字符')
        ]
    )

    subimt = SubmitField(label='登录')


class RegisterForm(FlaskForm):
    """注册表单"""
    name = StringField(
        label='名字',
        validators=[
            DataRequired(message='名字不能为空')
        ]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=3, message='密码至少包括 3 个字符')
        ]
    )

    subimt = SubmitField(label='登录')
