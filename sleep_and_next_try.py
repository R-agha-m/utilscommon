from time import sleep
from datetime import datetime, timedelta
from stg import report


def sleep_and_next_try(sleep_time,
                       force_report=False):
    if sleep_time:
        if force_report:
            print(f'sleep time: {sleep_time}')
            next_try = datetime.now() + timedelta(seconds=sleep_time)
            print(f'next try: {next_try}')
        else:
            report.debug(f'sleep time: {sleep_time}')
            next_try = datetime.now() + timedelta(seconds=sleep_time)
            report.debug(f'next try: {next_try}')

        sleep(sleep_time)
