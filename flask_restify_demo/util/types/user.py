# -*- coding: utf-8 -*-

from flask_restify import fields

from .date import Timestamp

from flask_restify_demo.util import strutil


class Email(fields.String):
    example = "user@o.oo"
    pattern = strutil.EMAIL_REGEX


class Password(fields.String):
    example = "*D821809F681A40A6E379B50D0463EFAE20BDD122"
    length = 41
