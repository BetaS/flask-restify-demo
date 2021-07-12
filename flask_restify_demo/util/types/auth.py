# -*- coding: utf-8 -*-

from flask_restify import fields
from flask_restify_demo.app.config import __DEFAULT_KEY__


class Authkey(fields.JWT):
    signature = __DEFAULT_KEY__


class SessionInfo(fields.Object):
    data = {
        "id": fields.Integer(),
        "email": fields.String(),
        "level": fields.String()
    }
