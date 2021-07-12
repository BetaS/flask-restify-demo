from flask_restify_demo.app import controller

from flask_restify_demo.models.board import BoardModel


class BoardController(controller.BaseController):
    model = BoardModel
