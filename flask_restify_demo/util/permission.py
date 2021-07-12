
def check_debug(context) -> bool:
    if context.user_id() in [1, 2, 3]:
        return True

    return False
