# -*- coding: utf-8 -*-

from flask_restify_demo.app import api
from flask_restify_demo.app.config import DevelopmentConfig, ProductionConfig

from flask_restify_demo import service

if not service:
    raise Exception("endpoint 가 정상 형성되지 않음")


if __name__ == '__main__':
    server = api.init_server(DevelopmentConfig)
    # server.run("0.0.0.0", 5001, use_reloader=False)
    server.run("0.0.0.0", 5000)

else:
    server = api.init_server(ProductionConfig)
