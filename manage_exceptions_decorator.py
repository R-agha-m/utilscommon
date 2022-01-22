from functools import wraps
from traceback import format_exc
import stg
# todo: get finally function


def manage_exceptions_decorator(caught_exceptions=(Exception,),
                                raised_exceptions=(),
                                report_traceback=True,
                                return_value=None):

    if stg.DEBUG_MODE:
        report_traceback = True

    def inner_decorator(func):
        @wraps(func)
        def wrapper(*func_args, **func_kwargs):
            try:
                return func(*func_args, **func_kwargs)
            except raised_exceptions as e:
                raise e

            except caught_exceptions:
                if report_traceback:
                    stg.report.warning(format_exc())
                return return_value

        return wrapper

    return inner_decorator


if __name__ == "__main__":
    @manage_exceptions_decorator()
    def ali():
        1/0

    ali()
