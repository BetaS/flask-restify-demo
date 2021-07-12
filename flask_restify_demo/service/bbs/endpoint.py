# -*- coding: utf-8 -*-

from flask_restify_demo.app import namespace, api
from flask_restify_demo.service.bbs.controller import board

from flask_restify import fields
from flask_restify.resource import restify

import datetime


bbs_ns = namespace.BaseNamespace(api, tag="bbs", path="/bbs", description="bullet-in board system api")


@restify.route(bbs_ns, method="GET", path="/<name>/", description="BBS글 조회")
@restify.parameter(path={
    "name": fields.String(description="게시판 ID")
}, query={
    "page": fields.Integer(default=1),
    "pagesize": fields.Integer(default=20)
})
@restify.response(description="상세정보", model={
    "timestamp": fields.Float(description="서버의 현재 타임스템프")
})
def list_bbs_items(context, name, page, pagesize):
    time = datetime.datetime.now()

    return {"timestamp": time.timestamp()}


@restify.route(bbs_ns, method="POST", path="/<name>/", description="BBS글 조회")
@restify.parameter(path={
    "name": fields.String(description="게시판 ID")
}, body={
    "title": fields.String(),
    "body": fields.String(optional=True)
})
@restify.response(201, description="상세정보")
def post_bbs_items(context, name, title, body):
    controller.create(name=name, title=title, body=body)

    return None, 201