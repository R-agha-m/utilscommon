from utilscommon.utilscommon.sleep import Sleep
from time import sleep

from threading import Thread

x = True


def listener_test():
    global x

    return x


sleep_obj = Sleep(sleep_time_absolute=8,
                  report_func=print,
                  sleep_func=sleep,
                  listener=listener_test)

thread_obj = Thread(target=sleep_obj.sleep,
                    kwargs=dict(),
                    name='sleep_time_with_listener')
thread_obj.start()

sleep(10)
x = False
