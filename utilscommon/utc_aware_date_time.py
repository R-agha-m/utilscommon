from datetime import datetime
from pytz import UTC


class UtcAwareDateTime(datetime):

    def __new__(
            cls,
            year,
            month=None,
            day=None,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
            tzinfo=None,
            *,
            fold=0,
    ):
        return super().__new__(
            cls,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=microsecond,
            tzinfo=UTC,
            fold=fold,
        )

