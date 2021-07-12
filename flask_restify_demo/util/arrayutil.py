# -*- coding: utf-8 -*-

from typing import Tuple


def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in range(0, len(l), n)]


def find_diff(origin: list, target: list) -> Tuple[set, set]:
    newed = set(target) - set(origin)
    removed = set(origin) - set(target)

    return newed, removed

