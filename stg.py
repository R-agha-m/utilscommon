from os import environ
from .global_stg_loader import global_stg_loader

GlobalStg = global_stg_loader(current_stg_address=__file__,
                              stg_class_name="LocalStg")


class LocalStg:
    _debug_mode = None
    _report = None
    _time_out = None
    _max_try = None
    _poll_frequency = None
    _implicit_wait_time = None

    @property
    def DEBUG_MODE(self):
        if self._debug_mode is None:
            from .detect_boolean import detect_boolean
            self._debug_mode = detect_boolean(
                environ.get("DEBUG_MODE",
                            True))
        return self._debug_mode

    @property
    def report(self):
        if self._debug_mode is None:
            from utils_logging.get_or_create_logger import get_or_create_logger
            self._report = get_or_create_logger(
                destinations=("console",),
                level=10 if self.DEBUG_MODE else 20
            )
        return self._report

    @property
    def TIME_OUT(self):
        if self._time_out is None:
            self._time_out = 10
        return self._time_out

    @property
    def MAX_TRY(self):
        if self._max_try is None:
            self._max_try = 10
        return self._max_try

    @property
    def POLL_FREQUENCY(self):
        if self._poll_frequency is None:
            self._poll_frequency = 0.1
        return self._poll_frequency

    @property
    def IMPLICIT_WAIT_TIME(self):
        if self._implicit_wait_time is None:
            self._implicit_wait_time = 10
        return self._implicit_wait_time


class StgClass(GlobalStg, LocalStg):
    pass


STG = StgClass()
report = STG.report

if __name__ == "__main__":
    print(STG.DEBUG_MODE)
    print(STG.report)
