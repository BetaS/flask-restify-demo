from flask_restify_demo.app import namespace, api


users_ns = namespace.BaseNamespace(api, tag="user", path="/users", description="유저 관리")


from . import users
