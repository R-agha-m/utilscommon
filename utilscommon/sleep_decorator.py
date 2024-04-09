from time import sleep
from functools import wraps
from .sleep import Sleep


def sleep_decorator(before=True,
                    after=True,
                    **kwargs):

    sleep_obj = Sleep(**kwargs)

    def inside(demand_func):
        wraps(demand_func)

        def wrapper(*args, **kwargs):
            if before:
                sleep_obj.sleep()

            result = demand_func(*args, **kwargs)

            if after:
                sleep_obj.sleep()

            return result

        return wrapper

    return inside
