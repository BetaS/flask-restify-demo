# -*- coding: utf-8 -*-

from contextlib import contextmanager

from flask_restify_demo.app import api, config


@contextmanager
def query_debugger(*args, **kwargs):
    server = api.init_server(config.QueryDebugConfig)

    with server.test_request_context():
        yield api.db
