# -*- coding: utf-8 -*-

from flask_restify_demo import app

from ._users import UserController


users = UserController(db=app.api.db)
