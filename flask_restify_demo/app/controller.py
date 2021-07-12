# -*- coding: utf-8 -*-

from typing import Optional
from contextlib import contextmanager

from flask_restify_demo.util import exceptions, queryutil


class BaseController:
    model = None
    db = None
    instant_commit = True
    primary_key = None

    def __init__(self, db):
        self.db = db
        self.instant_commit = True

        if self.primary_key:
            self.primary_key = getattr(self.model, self.primary_key)
        else:
            self.primary_key = self.model.idx

    @classmethod
    @contextmanager
    def debugger(cls, debug=True):
        from flask_restify_demo import api
        from flask_restify_demo.app.config import QueryDebugConfig, DevelopmentConfig

        if debug:
            server = api.init_server(QueryDebugConfig)
        else:
            server = api.init_server(DevelopmentConfig)

        with server.test_request_context():
            yield cls(db=api.db)

    def _standby(self):
        self.instant_commit = False

    def _commit(self):
        self.db.session.commit()

    def query(self):
        return self.model.query

    def on_pre_create(self, item: model, **kwargs) -> model:
        return item

    def on_post_create(self, item: model):
        pass

    def on_pre_update(self, item: model, **kwargs):
        pass

    def on_post_update(self, item: model, **kwargs):
        pass

    def on_pre_delete(self, item: model):
        pass

    def on_post_delete(self, item: model):
        pass

    def create(self, **kwargs) -> model:
        item = self.model(**kwargs)

        item = self.on_pre_create(item, **kwargs)

        # DB에 등록
        self.db.session.add(item)
        self.db.session.flush()

        if self.on_post_create(item):
            self.db.session.flush()

        return item

    def exist_id(self, idx: int) -> bool:
        return self.exist(where=(self.primary_key == idx))

    def exist(self, where) -> bool:
        return bool(self.db.session.query(self.model.query.filter(where).exists()).scalar())

    def get(self, idx: int, **kwargs) -> Optional[model]:
        return self.find(where=self.primary_key == idx, **kwargs)

    def find(self, where, **kwargs) -> Optional[model]:
        base = self.query()

        base = queryutil.build_query(base, **kwargs)

        return base.filter(where).first()

    def set(self, idx: int, info: dict) -> model:
        item = self.get(idx)

        if item is None:
            raise exceptions.NotFoundException("아이템을 찾을 수 없습니다.")

        self.on_pre_update(item, **info)
        queryutil.setall(item, info)
        self.on_post_update(item, **info)
        self.db.session.flush()

        return item

    def update(self, idx: int, info: dict) -> model:
        item = self.get(idx)

        if item is None:
            raise exceptions.NotFoundException("아이템을 찾을 수 없습니다.")

        self.on_pre_update(item, **info)
        queryutil.update(item, info)
        self.on_post_update(item, **info)
        self.db.session.flush()

        return item

    def delete(self, idx: int) -> bool:
        item = self.get(idx)

        if item is None:
            raise exceptions.NotFoundException("아이템을 찾을 수 없습니다.")

        self.on_pre_delete(item)

        self.db.session.delete(item)
        self.db.session.flush()

        self.on_post_delete(item)

        return True

    def delete_all(self, where):
        items, _ = self.search(where=where)

        for item in items:
            try:
                self.on_pre_delete(item)
            except Exception:
                pass

            self.db.session.delete(item)
            self.on_post_delete(item)

        self.db.session.flush()

    def search(self, **kwargs) -> ([model], int):
        base = self.query()

        base = queryutil.build_query(base, **kwargs)

        if "page" in kwargs and kwargs["page"] is not None:
            page = kwargs["page"]
            pagesize = 10
            if "pagesize" in kwargs and kwargs["pagesize"] is not None:
                if kwargs["pagesize"] > 50:
                    raise exceptions.NotFoundException()

                pagesize = kwargs["pagesize"]

            return queryutil.pagination(base, page, pagesize)
        else:
            return base.all(), 0

    def count(self, **kwargs) -> int:
        base = self.query()
        base = queryutil.build_query(base, **kwargs)

        return base.count()

    def execute(self, sql: str):
        return self.db.engine.execute(sql)
