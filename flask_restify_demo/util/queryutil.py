# -*- coding: utf-8 -*-

from flask_restify_demo.util import exceptions, strutil

from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy import func


def build_query(base, **kwargs):
    if "column" in kwargs and kwargs["column"] is not None:
        if type(kwargs["column"]) in (tuple, list):
            base = base.with_entities(*kwargs["column"])
        else:
            base = base.with_entities(kwargs["column"])

    if "distinct" in kwargs and kwargs["distinct"] is not None:
        if type(kwargs["distinct"]) in (tuple, list):
            base = base.distinct(*kwargs["distinct"])
        else:
            base = base.distinct(kwargs["distinct"])

    if "join" in kwargs and kwargs["join"] is not None:
        if type(kwargs["join"]) in (tuple, list):
            for j in kwargs["join"]:
                if type(j) == tuple:
                    if j[1]:
                        if len(j) == 3:
                            base = base.outerjoin((j[0], j[2]))
                        else:
                            base = base.outerjoin(j[0])
                    else:
                        if len(j) == 3:
                            base = base.join((j[0], j[2]))
                        else:
                            base = base.join(j[0])
                else:
                    base = base.join(j)
        else:
            base = base.join(kwargs["join"])

    if "where" in kwargs and kwargs["where"] is not None:
        if type(kwargs["where"]) in (tuple, list):
            base = base.filter(*kwargs["where"])
        else:
            base = base.filter(kwargs["where"])

    if "order" in kwargs and kwargs["order"] is not None:
        if type(kwargs["order"]) in (tuple, list):
            base = base.order_by(*kwargs["order"])
        else:
            base = base.order_by(kwargs["order"])

    if "group" in kwargs and kwargs["group"] is not None:
        if type(kwargs["group"]) in (tuple, list):
            base = base.group_by(*kwargs["group"])
        else:
            base = base.group_by(kwargs["group"])

    if "options" in kwargs and kwargs["options"] is not None:
        if type(kwargs["options"]) in (tuple, list):
            base = base.options(*kwargs["options"])
        else:
            base = base.options(kwargs["options"])

    return base


def setall(base, data):
    for key, value in data.items():
        setattr(base, key, value)
        flag_modified(base, key)


def update(base, data):
    for key, value in data.items():
        if isinstance(getattr(base, key, None), dict) and type(value) == dict:
            getattr(base, key).update(value)
        else:
            setattr(base, key, value)

        flag_modified(base, key)


def pagination(base, page, pagesize) -> ([], int):
    start = (page - 1) * pagesize
    end = (page - 1) * pagesize + pagesize

    return base.slice(start, end).all(), int((base.count() - 1) / pagesize) + 1


def add_filter(filter, stmt, _or=False):
    if filter is None:
        return stmt
    else:
        if _or:
            return filter | stmt
        else:
            return filter & stmt


def get_current(old, new, key: str):
    return new.get(key) if key in new else getattr(old, key)
