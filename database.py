# -*- coding: utf-8 -*-
from flask_restify_demo.models import db

from sqlalchemy import Table


def drop_all():
    sess = db.session()
    meta = db.metadata

    print([k.fullname for k in meta.sorted_tables])

    db.drop_all()

    sess.commit()


if __name__ == "__main__":
    from flask_restify_demo.app import api, config

    from flask_restify_demo.models import user

    server = api.init_server(config.QueryDebugConfig)

    with server.test_request_context():
        tbls = [
            user.UsersModel
        ]

        for tbl in tbls:
            if isinstance(tbl, Table):
                tbl.create(bind=api.db.engine, checkfirst=True)
            else:
                tbl.__table__.create(bind=api.db.engine, checkfirst=True)
