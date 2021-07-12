# -*- coding: utf-8 -*-

from flask_restify.resource import namespace

from .context import Context


class BaseNamespace(namespace.Namespace):
    __PREFIX__ = "/api/v1"

    def __init__(self, api, tag, path, description):
        super().__init__(api, tag, self.__PREFIX__+path, description, context=Context)
