import pytz
from datetime import datetime

MOSCOW_TIMEZONE = pytz.timezone('Europe/Moscow')


def time_control(time_from: int, time_to: int):
    def decorator(func, *args, **kwargs):
        def wrapped(*args, **kwargs):
            if datetime.now(MOSCOW_TIMEZONE).hour < time_from or datetime.now(MOSCOW_TIMEZONE).hour > time_to:
                return
            else:
                func(*args, **kwargs)
        return wrapped
    return decorator
