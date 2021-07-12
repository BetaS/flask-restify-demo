# -*- coding: utf-8 -*-

from flask_restify_demo.app import namespace, api

from flask_restify import fields
from flask_restify.resource import restify

import datetime


common_ns = namespace.BaseNamespace(api, tag="common", path="/common", description="Common Action")


@restify.route(common_ns, method="GET", path="/check", description="API 상태 체크")
@restify.response(description="상세정보", model={
    "timestamp": fields.Float(description="서버의 현재 타임스템프"),
    "my_ip": fields.String(description="내 IP 주소")
})
def check_status(context):
    time = datetime.datetime.now()

    return {"timestamp": time.timestamp(), "my_ip": context.ip_addr()}
