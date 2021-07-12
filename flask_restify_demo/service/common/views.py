
from flask_restify import fields


class CodeItemView(fields.Object):
    data = {
        "code": fields.Integer(description="코드 ID"),
        "name": fields.String(description="코드 설명")
    }
