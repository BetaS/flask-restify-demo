# -*- coding: utf-8 -*-

from flask_restify.api import BaseAPI


class API(BaseAPI):
    _callbacks = []

    def init_func(self, callback):
        self._callbacks.append(callback)

    def on_init(self):
        for callback in self._callbacks:
            callback()

    def on_exit(self):
        pass

    def on_error(self, context, e):
        self.db.session.rollback()


api = API("flask-restify Simple API", "Demo API for flask-restify.", "1.0.0")