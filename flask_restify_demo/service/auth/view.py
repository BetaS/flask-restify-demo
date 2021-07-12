from flask_restify_demo.models.user import UsersModel

from flask_restify import fields


class AuthUserModelView(fields.Object):
    data = {
        "idx": fields.Integer(description="user idx"),
        "name": fields.String(description="사용자 이름"),
    }

    @classmethod
    def view(cls, user: UsersModel):
        return {
            "idx": user.idx,
            "name": user.name
        }


class AuthDataModelView(fields.Object):
    data = {
        "user": AuthUserModelView(),
    }

    @classmethod
    def view(cls, user: UsersModel):
        return {
            "user": AuthUserModelView.view(user)
        }
