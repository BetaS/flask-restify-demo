# -*- coding: utf-8 -*-

from ..app import api
from .common.endpoint import common_ns
from .bbs.endpoint import bbs_ns
from .auth.endpoint import auth_ns


def register_endpoints():
    api.add_namespace(common_ns)
    api.add_namespace(bbs_ns)
    api.add_namespace(auth_ns)


api.init_func(register_endpoints)
