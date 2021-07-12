from flask_restify import fields


class Page(fields.Integer):
    description = "페이지 번호"
    default = 1


class PageSize(fields.Integer):
    description="페이지 사이즈"
    default = 20


class PagedDocument(fields.Object):
    data = {
        "page": fields.Integer(description="호출 한 페이지 번호"),
        "max_page": fields.Integer(description="최대 페이지 크기"),
        "items": fields.Array(description="결과값")
    }

    def __init__(self, item, **kwargs):
        super().__init__(**kwargs)

        self.data = {
            **self.data,
            "items": fields.Array(item=item, description="결과값")
        }

    @classmethod
    def view(cls, page, max_page, items):
        return {
            "page": page,
            "max_page": max_page,
            "items": items
        }