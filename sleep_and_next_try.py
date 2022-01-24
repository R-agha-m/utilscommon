from time import sleep
from datetime import datetime, timedelta
from .stg import report


def sleep_and_next_try(sleep_time):
    if sleep_time:
        report.info(f'sleep time: {sleep_time}')
        next_try = datetime.now() + timedelta(seconds=sleep_time)
        report.info(f'next try: {next_try}')
        sleep(sleep_time)
