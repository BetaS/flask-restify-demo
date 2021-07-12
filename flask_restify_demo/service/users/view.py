# -*- coding: utf-8 -*-

from flask_restify_demo.util import types

from flask_restify_demo.models.user import UsersModel

from flask_restify import fields


insert_params = {
    "login_id": fields.String(description="아이디"),
    "login_pw": types.user.Password(description="비밀번호"),
    "name": fields.String(description="사용자 이름"),
    "email": types.user.Email(description="이메일 주소"),
    "phone": fields.String(description="핸드폰번호", optional=True)
}


update_params = {
    "name": fields.String(description="사용자 이름"),
    "email": types.user.Email(description="이메일 주소"),
    "phone": fields.String(description="핸드폰번호", optional=True)
}


class UserSummaryView(fields.Object):
    data = {
        "idx": fields.Integer(description="사용자 UID"),
        "login_id": fields.String(description="로그인 ID"),
        "name": fields.String(description="사용자 이름"),
        "email": types.user.Email(description="이메일 주소"),
        "phone": fields.String(description="핸드폰번호", optional=True),
        "insert_date": types.date.DateTime(description="가입일")
    }

    @classmethod
    def view(cls, user: UsersModel):
        return {
            "idx": user.idx,
            "login_id": user.login_id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "insert_date": types.date.DateTime.mapping(user.insert_date),
        }
