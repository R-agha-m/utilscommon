from multiprocessing import freeze_support
from .processUtils.lof import ProcessWithExceptionCatcher
from functools import wraps
from time import sleep
from datetime import datetime
from .exception import ExceptionInChildProcess
from datetime import timedelta
import stg


def run_func_4_duration(dead_time=None,
                        sleep_between_each_check=None,
                        raise_=True):

    dead_time = dead_time or stg.TIME_OUT
    sleep_between_each_check = sleep_between_each_check if sleep_between_each_check is not None else stg.POLL_FREQUENCY

    if type(dead_time) in (int, float):
        dead_time = datetime.now() + timedelta(seconds=dead_time)

    def inside(demand_func):
        wraps(demand_func)

        def wrapper(*args, **kwargs):
            freeze_support()
            process = ProcessWithExceptionCatcher(target=demand_func,
                                                  args=args,
                                                  kwargs=kwargs)
            process.start()

            while process.is_alive() and (datetime.now() < dead_time):
                sleep(sleep_between_each_check)

            if raise_ and process.exception:
                raise ExceptionInChildProcess(traceback=process.exception[1]) from process.exception[0]

            process.terminate()

            return None

        return wrapper

    return inside
