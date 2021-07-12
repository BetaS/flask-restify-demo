# -*- coding: utf-8 -*-

from flask_restify_demo.app import namespace, api
from flask_restify_demo.util import exceptions, permission, types
from flask_restify_demo.service.users.controller import users
from flask_restify_demo.service.auth.controller import create_user_auth, update_auth

from flask_restify_demo.service.auth.view import AuthDataModelView

from flask_restify import fields
from flask_restify.resource import restify


auth_ns = namespace.BaseNamespace(api, tag="auth", path="/auth", description="authentication api")


@restify.route(auth_ns, method="POST", path="/", description="login")
@restify.parameter(body={
    "login_id": fields.String(description="아이디"),
    "login_pw": types.user.Password(description="패스워드")
})
@restify.response(201, "성공", model=AuthDataModelView())
@restify.error(404, "해당 회원 정보를 찾을 수 없습니다.", exceptions.NotFoundException)
def login_user(context, login_id, login_pw):
    info = users.login(login_id, login_pw)

    if not info:
        raise exceptions.NotFoundException("유저 정보를 조회 할 수 없습니다.")

    data, authkey = create_user_auth(info)
    context.set_authkey(authkey)

    return data, 201


@restify.route(auth_ns, method="GET", path="", description="인증 확인")
@restify.authenticate()
@restify.response(200, "성공", model=AuthDataModelView())
@restify.error(404, "해당 회원 정보를 찾을 수 없습니다.", exceptions.NotFoundException)
def authenticate(context):
    info = context.session

    for k in ("jti", "iat", "nbf", "exp"):
        if k in info:
            del info[k]

    return info