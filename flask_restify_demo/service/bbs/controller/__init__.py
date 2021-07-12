from flask_restify_demo import app

from ._board import BoardController


board = BoardController(db=app.api.db)