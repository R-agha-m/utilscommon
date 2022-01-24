from functools import wraps
from traceback import format_exc
from time import sleep
try:
    from .stg import STG, report
except ImportError:
    from stg import STG, report


def repetition_decorator(repetition=None,
                         caught_exceptions=(Exception,),
                         raised_exceptions=(),
                         sleep_between_each=None):

    repetition = repetition or STG.MAX_TRY
    sleep_between_each = sleep_between_each or STG.POLL_FREQUENCY

    def inside(demand_func):
        wraps(demand_func)

        def wrapper(*args, **kwargs):
            for index in range(1, repetition + 1):
                report.debug(f'repetition no. {index}')
                try:
                    if "rep_index" in demand_func.__code__.co_varnames:
                        kwargs["rep_index"] = index
                    return demand_func(*args, **kwargs)
                except raised_exceptions as e:
                    raise e

                except caught_exceptions as e:
                    if index < repetition:
                        report.warning(format_exc())
                        sleep(sleep_between_each)
                    else:
                        report.error(format_exc())
                        raise e

        return wrapper

    return inside
