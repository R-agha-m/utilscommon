from os import _exit  # noqa
from sys import exit as sys_exit
try:
    from .manage_exceptions_decorator import manage_exceptions_decorator
except ImportError:
    from manage_exceptions_decorator import manage_exceptions_decorator


@manage_exceptions_decorator()
def exit_():
    try:
        sys_exit(0)
    except SystemExit:
        _exit(0)
