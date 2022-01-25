from pyvirtualdisplay import Display
try:
    from .manage_exceptions_decorator import manage_exceptions_decorator
except ImportError:
    from manage_exceptions_decorator import manage_exceptions_decorator


class VirtualDisplay(Display):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __del__(self):
        self._stop_virtual_display()
        # super().__del__()

    @manage_exceptions_decorator()
    def _stop_virtual_display(self):
        self.stop()
