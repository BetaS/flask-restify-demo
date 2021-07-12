# -*- coding: utf-8 -*-

from flask_restify_demo.app import api
from flask_restify_demo.app.config import Config

from flask_restify_demo.service.auth.view import AuthDataModelView

from flask_restify_demo.models.user import UsersModel

from flask_restify_demo.util import exceptions

import jwt
import datetime
import string
import random


__SESSION_VALIDATE_TIME__ = 7*24


def random_string(length: int) -> str:
    letters = string.ascii_letters+string.digits
    return ''.join(random.choice(letters) for i in range(length))


def create_user_auth(user, company_info=None, role=None):
    # authkey 생성
    if user.authkey is None:
        authkey = random_string(16)
    else:
        authkey = user.authkey

    session = {
        "jti": authkey,
        "iat": datetime.datetime.utcnow(),
        "nbf": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=__SESSION_VALIDATE_TIME__),
    }

    data = AuthDataModelView.view(user, company_info, role)

    session.update(data)

    # DB에 업데이트
    user.authkey = authkey
    user.last_auth = session["iat"]
    api.db.session.flush()

    return data, _encode(session)


def check_auth(authcode):
    # authcode가 정상적인지 검증해서 회원의 권한 정보를 반환
    info = _decode(authcode)

    # DB의 토큰 값과 일치하는지 비교
    user = UsersModel.query.with_entities(UsersModel.authkey).filter_by(idx=info["user"]["idx"], is_exit='0').first()

    if user is None:
        raise exceptions.NoPermissionException("해당 사용자를 찾을 수 없음")

    if "jti" in info and info["jti"] is not None:
        if user.authkey != info["jti"]:
            raise jwt.exceptions.InvalidIssuedAtError("로그인 NONCE 값이 일치하지 않음")
    else:
        raise jwt.exceptions.InvalidIssuedAtError("로그인 NONCE 값이 없음")

    return info


def update_auth(authcode):
    info = _decode(authcode)

    if "exp" in info:
        info["exp"] = datetime.datetime.utcnow() + datetime.timedelta(hours=__SESSION_VALIDATE_TIME__)

        return _encode(info)

    return authcode


def _decode(authcode):
    return jwt.decode(authcode, Config.JWT_SECRET, algorithms='HS256')


def _encode(data):
    # return str(jwt.encode(data, Config.JWT_SECRET, algorithm='HS256'), encoding="utf-8")
    return jwt.encode(data, Config.JWT_SECRET, algorithm='HS256')
