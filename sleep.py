from time import sleep, time
from datetime import datetime, timedelta


class Sleep:
    def __init__(self,
                 sleep_time_absolute=None,
                 sleep_time_mean=1,
                 sleep_time_std=None,
                 sleep_time_cov=0.25,
                 sleep_time_minimum=None,
                 sleep_time_maximum=None,
                 logger=None,
                 sleep_func=sleep,
                 sleep_func_args=tuple(),
                 sleep_func_kwargs=dict(),
                 listener_func=None,
                 listener_func_args=tuple(),
                 listener_func_kwargs=dict()):

        self.sleep_time_absolute = sleep_time_absolute
        self.logger = logger
        self.sleep_func = sleep_func
        self.sleep_func_args = sleep_func_args
        self.sleep_func_kwargs = sleep_func_kwargs
        self.sleep_time_mean = sleep_time_mean
        self.sleep_time_std = sleep_time_std
        self.sleep_time_cov = sleep_time_cov
        self.sleep_time_minimum = sleep_time_minimum
        self.sleep_time_maximum = sleep_time_maximum
        self.listener_func = listener_func
        self.listener_func_args = listener_func_args
        self.listener_func_kwargs = listener_func_kwargs

    _sleep_time = None

    @property
    def sleep_time(self):
        if self._sleep_time is None:
            if self.sleep_time_absolute is None:
                self.calculate_random_sleep_time()
            else:
                self._sleep_time = self.sleep_time_absolute
        return self._sleep_time

    _sleep_time_std = None

    @property
    def sleep_time_std(self):
        if self._sleep_time_std is None:
            self._sleep_time_std = self.sleep_time_cov * self.sleep_time_mean
        return self._sleep_time_std

    @sleep_time_std.setter
    def sleep_time_std(self, sleep_time_std):
        self._sleep_time_std = sleep_time_std

    _sleep_time_minimum = None

    @property
    def sleep_time_minimum(self):
        if self._sleep_time_minimum is None:
            self._sleep_time_minimum = max(0, self.sleep_time_mean - 2 * self.sleep_time_std)
        return self._sleep_time_minimum

    @sleep_time_minimum.setter
    def sleep_time_minimum(self, sleep_time_minimum):
        self._sleep_time_minimum = sleep_time_minimum

    _sleep_time_maximum = None

    @property
    def sleep_time_maximum(self):
        if self._sleep_time_maximum is None:
            self._sleep_time_maximum = self.sleep_time_mean + 2 * self.sleep_time_std
        return self._sleep_time_maximum

    @sleep_time_maximum.setter
    def sleep_time_maximum(self, sleep_time_maximum):
        self._sleep_time_maximum = sleep_time_maximum

    def calculate_random_sleep_time(self):
        from numpy.random import normal
        sleep_time = float(normal(self.sleep_time_mean, self.sleep_time_std, 1))
        return round(max(min(sleep_time, self.sleep_time_maximum), self.sleep_time_minimum), 1)

    @property
    def next_try(self):
        return datetime.now() + timedelta(seconds=self.sleep_time)

    def report(self):
        if self.logger:
            self.logger.debug(f'sleep time: {self.sleep_time} (s)  -> next try: {self.next_try}')

    def sleep(self):
        if self.listener_func:
            self.sleep_with_listener()
        else:
            self.sleep_without_listener()

    def sleep_without_listener(self):
        self.report()
        self.sleep_func(self.sleep_time, *self.sleep_func_args, **self.sleep_func_kwargs)

    def sleep_with_listener(self):
        now = time()
        self.report()
        future = now + self.sleep_time

        while time() < future:
            if self.listener_func(*self.listener_func_args, **self.listener_func_kwargs):
                # print(time()-now)
                self.sleep_func(1, *self.sleep_func_args, **self.sleep_func_kwargs)
            else:
                # print("break")
                break
        # else:
        # print("finish")
