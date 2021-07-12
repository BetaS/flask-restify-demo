# -*- coding: utf-8 -*-

from flask_restify import fields
from flask import request


class I18N(fields.Object):
    data = {
        "ko": fields.String(description="한국어", optional=True),
        "en": fields.String(description="영어", optional=True),
        "jp": fields.String(description="일본어", optional=True),
        "zh": fields.String(description="중국어", optional=True),
    }

    @classmethod
    def mapping(cls, value: dict, lang=None):
        if lang is None:
            lang = request.accept_languages.best

        if lang is None or lang == "*":
            return value
        else:
            if isinstance(value, dict):
                for i in (lang, "ko", "en", "jp", "zh"):
                    if i in value:
                        return value[i]

                return None
            else:
                return value
