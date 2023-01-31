from functools import wraps
from traceback import format_exc
from time import sleep


def repetition_decorator(repetition=None,
                         caught_exceptions=(Exception,),
                         raised_exceptions=(),
                         sleep_between_each=None,
                         sleep_func=sleep,
                         logger=None):

    def inside(demand_func):
        wraps(demand_func)

        def wrapper(*args, **kwargs):
            for index in range(1, repetition + 1):
                if logger:
                    logger.debug(f'repetition no. {index}')
                try:
                    if "rep_index" in demand_func.__code__.co_varnames:
                        kwargs["rep_index"] = index
                    return demand_func(*args, **kwargs)
                except raised_exceptions as e:
                    raise e

                except caught_exceptions as e:
                    if index < repetition:
                        logger.debug(format_exc())
                        sleep_func(sleep_between_each)
                    else:
                        logger.warning(format_exc())
                        raise e

        return wrapper

    return inside
