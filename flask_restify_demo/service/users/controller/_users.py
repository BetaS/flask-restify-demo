from flask_restify_demo.app import controller
from flask_restify_demo.util import exceptions, queryutil, strutil

from flask_restify_demo.models.user import UsersModel

from sqlalchemy import func


class UserController(controller.BaseController):
    model = UsersModel

    def on_pre_create(self, item: model, **kwargs) -> model:
        # 중복된 이메일 있는지 체크
        if self.exist(UsersModel.login_id == item.login_id):
            raise exceptions.AlreadyExistException("해당 아이디는 중복됩니다.")

        return item

    def on_pre_update(self, item: model, **kwargs):
        queryutil.no_edit(kwargs, ["authkey"])

        if "login_pw" in kwargs:
            item.authkey = strutil.random_string(16)

    def check_id(self, login_id: str) -> bool:
        return super().exist(where=(UsersModel.login_id == login_id))

    def login(self, login_id: str, login_pw: str):
        where = None
        where = queryutil.add_filter(where, UsersModel.login_id == login_id)
        where = queryutil.add_filter(where, UsersModel.login_pw == login_pw)
        where = queryutil.add_filter(where, UsersModel.is_exit == False)

        return self.find(where=where)

    def exit(self, idx: int) -> bool:
        item = self.get(idx)

        self.update(idx, {
            # "login_id": "*"+item.login_id,
            "is_exit": True,
            "exit_date": func.now()
        })

        return True


if __name__ == "__main__":
    with UserController.debugger() as controller:
        result = controller.login("tester", "*6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9")
        print(result)
