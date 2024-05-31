from time import sleep
from datetime import datetime
from asyncio import sleep as asyncio_sleep

def sleep_until(target_time: datetime):
    # Calculate the difference between the target time and now
    time_diff = (target_time - datetime.utcnow()).total_seconds()

    # If the target time is in the past, no need to sleep
    if time_diff > 0:
        sleep(time_diff)


async def async_sleep_until(target_time: datetime):
    # Calculate the difference between the target time and now
    time_diff = (target_time - datetime.utcnow()).total_seconds()

    # If the target time is in the past, no need to sleep
    if time_diff > 0:
        await asyncio_sleep(time_diff)


if __name__ == '__main__':
    from datetime import timedelta

    now = datetime.utcnow()
    print(now)
    # Define the target time (example: sleep until 23:00 today)
    target_time_ = datetime.utcnow() + timedelta(minutes=1)
    print(target_time_)
    sleep(10)
    # Call the function
    sleep_until(target_time_)
    # Code to execute after waking up
    print(f"Woke up at the target time. {datetime.utcnow()}")
