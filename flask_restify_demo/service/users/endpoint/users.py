# -*- coding: utf-8 -*-
from . import users_ns


from flask_restify_demo.util import exceptions
from flask_restify_demo.service.users.controller import users

from flask_restify import fields
from flask_restify.resource import restify

from ..view import insert_params


@restify.route(users_ns, method="POST", path="/", description="수요자 회원가입")
@restify.parameter(body=insert_params)
@restify.response(201, "성공", model={
    "created_idx": fields.Integer(description="생성된 회원 idx, (UID)")
})
@restify.error(403, "회원을 생성하기 위한 권한이 없습니다.", exceptions.NoPermissionException)
@restify.error(404, "회원 생성의 경로를 찾을 수 없습니다.", exceptions.NotFoundException)
@restify.error(409, "이미 존재하는 회원 ID", exceptions.AlreadyExistException)
def sign_up_buyer(context, login_id, login_pw, name, email, **kwargs):
    if users.check_id(login_id):
        raise exceptions.AlreadyExistException("해당 아이디는 이미 존재합니다.")

    created_user = users.create(
        login_id=login_id,
        login_pw=login_pw,
        name=name,
        email=email,
        **kwargs
    )

    return {"created_idx": created_user.idx}, 201
