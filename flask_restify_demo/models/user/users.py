from sqlalchemy import Column, BIGINT, TEXT, JSON, BOOLEAN, DateTime, TIMESTAMP
from sqlalchemy.sql import func

from . import BaseModel, db


class UsersModel(BaseModel, db.Model):
    __tablename__ = "users"

    idx = Column(BIGINT, primary_key=True, autoincrement=True)
    login_id = Column(TEXT, nullable=False)
    login_pw = Column(TEXT, nullable=False)
    authkey = Column(TEXT)
    last_auth = Column(DateTime(timezone=True))
    name = Column(TEXT, nullable=False)
    email = Column(TEXT, nullable=False)
    phone = Column(TEXT)
    info = Column(JSON, server_default="{}", nullable=False)
    is_exit = Column(BOOLEAN, nullable=False, default=False)
    exit_date = Column(DateTime(timezone=True))
    insert_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    update_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        if self.is_exit:
            return f"[{self.gubun_name}] *{self.login_id} (탈퇴한 사용자)"
        return f"[{self.gubun_name}] {self.login_id} ({self.name}, ID:{self.idx})"