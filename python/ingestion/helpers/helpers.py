from datetime import datetime

def is_integer(value):
    try:
        if int(value) and int(value) < 2.1 * 10 ** 9:
            return True
        else:
            return False
    except ValueError:
        return False


def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_boolean(value):
    return value.lower() in {"true", "false"}


def is_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_timestamp(value):
    try:
        datetime.fromisoformat(value)
        return True
    except ValueError:
        return False