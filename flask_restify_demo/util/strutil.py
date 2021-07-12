# -*- coding: utf-8 -*-

import datetime
import string
import random
import json
import hashlib


EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


def money_string(i: float) -> str:
    return f"{i:,.2f}".rstrip('0').rstrip('.')


def parse_date(date: str) -> datetime.date:
    return datetime.datetime.strptime(date, '%Y-%m-%d').date()


def random_string(length: int) -> str:
    letters = string.ascii_letters+string.digits
    return ''.join(random.choice(letters) for i in range(length))


def mysql_password(pw: str) -> str:
    return "*" + hashlib.sha1(hashlib.sha1(pw.encode()).digest()).hexdigest().upper()


def mask_email(email: str, length: int=3) -> str:
    idx = email.find('@')
    start = idx - length - 1
    if start <= 0:
        start = 1
    end = idx - 1

    return email[:start] + "*"*(end-start) + email[end:]


def truncate(text: str, length: int = 20) -> str:
    return text[:length-2] + '...' if len(text) > length else text


def load_from_json(path: str):
    with open(path, 'r', encoding="utf-8") as fp:
        return json.load(fp)
