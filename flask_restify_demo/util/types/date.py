# -*- coding: utf-8 -*-

from flask_restify import fields
from typing import Optional
import datetime


class StrDate(fields.String):
    description = "날짜"
    example = "1990-01-01"
    length = 10
    regex = r'\d{4}-\d{2}-\d{2}'

    def validation(self, data):
        data = super().validation(data)

        if data:
            data = datetime.datetime.strptime(data, '%Y-%m-%d').date()
            return data.strftime("%Y-%m-%d")
        else:
            return None

    @classmethod
    def mapping(cls, data) -> Optional[str]:
        if data is None:
            return None

        return data.strftime("%Y-%m-%d")


class Date(fields.String):
    description = "날짜"
    example = "1990-01-01"
    length = 10
    regex = r'\d{4}-\d{2}-\d{2}'

    def validation(self, data):
        data = super().validation(data)

        if data:
            data = datetime.datetime.strptime(data, '%Y-%m-%d').date()

        return data

    @classmethod
    def mapping(cls, data) -> Optional[str]:
        if data is None:
            return None

        return data.strftime("%Y-%m-%d")


class DateTime(fields.String):
    description = "날짜&시간"
    example = "1990-01-01 00:00:00"
    length = 19
    regex = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

    def validation(self, data):
        data = super().validation(data)

        if data:
            data = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S").date()

        return data

    @classmethod
    def mapping(cls, data) -> str:
        return data.strftime("%Y-%m-%d %H:%M:%S")


class Timestamp(fields.Object):
    data = {
        "insert_date": fields.Integer(description="정보 등록일"),
        "update_date": fields.Integer(description="정보 수정일")
    }

    @classmethod
    def mapping(cls, data) -> {str: int}:
        return {
            "insert_date": int(data.insert_date.timestamp()),
            "update_date": int(data.update_date.timestamp())
        }
