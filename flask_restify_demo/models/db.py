from sqlalchemy.ext.declarative import declarative_base


def register(model):
    global Model
    Model = model


Model = declarative_base()
