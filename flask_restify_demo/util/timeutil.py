import datetime


KST = datetime.timezone(datetime.timedelta(hours=9))


def today():
    return datetime.datetime.now(tz=KST)

