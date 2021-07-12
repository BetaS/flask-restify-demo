# -*- coding: utf-8 -*-
from . import db, BaseModel

from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP, func


class BoardModel(BaseModel, db.Model):
    __tablename__ = "board"

    idx = Column(BIGINT, autoincrement=True, primary_key=True)

    title = Column(TEXT, nullable=False)
    desc = Column(TEXT)

    insert_date = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    update_date = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"{self.title} (ID:{self.idx})"
