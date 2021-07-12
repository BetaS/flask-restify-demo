from flask_restify_demo.app import api
from flask_restify_demo.models import db


db.register(api.db.Model)
