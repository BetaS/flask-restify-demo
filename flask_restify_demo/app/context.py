# -*- coding: utf-8 -*-

from flask_restify.resource.context import BaseContext

from flask_restify_demo.service.auth.controller import check_auth, update_auth

import random


class Context(BaseContext):
    session: dict = None
    authkey: str = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.session = None
        self.authkey = ""

        self.nonce = random.random()

    def user_id(self) -> int:
        if not self.session or "user" not in self.session:
            return 0
        else:
            return self.session["user"]["idx"]

    def on_auth(self):
        self.session = check_auth(self.authkey)

    def update_authkey(self, authkey):
        self.authkey = authkey

        if len(authkey) > 0:
            self.on_auth()

            self.authkey = update_auth(authkey)
            self.set_authkey(self.authkey)

    def ip_addr(self):
        from flask import request

        remote_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

        return remote_addr
