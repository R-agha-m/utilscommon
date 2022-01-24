from numpy.random import normal
from functools import wraps
from time import sleep
try:
    from .stg import STG
except ImportError:
    from stg import STG


def random_sleep(mean=1,
                 std=None,
                 cov=0.25,
                 minimum=None,
                 maximum=None,
                 do_sleep=True):

    if not std:
        std = cov * mean

    if not minimum:
        minimum = max(0, mean - 2 * std)

    if not maximum:
        maximum = mean + 2 * std

    sleep_time = float(normal(mean, std, 1))
    sleep_time = round(max(min(sleep_time, maximum), minimum), 1)
    report.debug(f'sleep time: {sleep_time}')

    if do_sleep:
        sleep(sleep_time)

    return sleep_time


def random_sleep_decorator(mean=1,
                           std=None,
                           cov=0.25,
                           minimum=None,
                           maximum=None,
                           do_sleep=True,
                           before=True,
                           after=True):
    def inside(demand_func):
        wraps(demand_func)

        def wrapper(*args, **kwargs):
            if before:
                random_sleep(mean=mean,
                             std=std,
                             cov=cov,
                             minimum=minimum,
                             maximum=maximum,
                             do_sleep=do_sleep)

            result = demand_func(*args, **kwargs)

            if after:
                random_sleep(mean=mean,
                             std=std,
                             cov=cov,
                             minimum=minimum,
                             maximum=maximum,
                             do_sleep=do_sleep)

            return result

        return wrapper

    return inside
