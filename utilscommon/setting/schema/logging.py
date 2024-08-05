from datetime import time
from typing import Optional, Any

from pydantic import (
    BaseModel,
    Field,
)
from ..enum import (
    EnumLogLevel,
    EnumLogHandler,
    EnumLogStream,
    EnumLogRotatingWhen,
    EnumLogFacilityCode,
    EnumLogSocketType,
)


class TimedRotatingFileHandler(BaseModel):
    def __init__(self, **data: Any):
        should_be_upper_list = ("WHEN",)
        for i in should_be_upper_list:
            if i in data:
                data[i] = data[i].upper()

        super().__init__(**data)

    FILENAME: Optional[str] = Field(default=None, serialization_alias='filename')
    WHEN: Optional[EnumLogRotatingWhen] = Field(default=None, serialization_alias='when')
    INTERVAL: Optional[int] = Field(default=None, serialization_alias='interval')
    BACKUP_COUNT: Optional[int] = Field(default=None, serialization_alias='backupCount')
    ENCODING: Optional[str] = Field(default=None, serialization_alias='encoding')
    DELAY: Optional[bool] = Field(default=None, serialization_alias='delay')
    UTC: Optional[bool] = Field(default=None, serialization_alias='utc')
    AT_TIME: Optional[time] = Field(default=None, serialization_alias='atTime')
    ERRORS: Optional[str] = Field(default=None, serialization_alias='errors')


class SysLogHandler(BaseModel):

    def __init__(self, **data: Any):
        should_be_upper_list = (
            "facility",
            "socktype",
        )
        for i in should_be_upper_list:
            if i in data:
                data[i] = data[i].upper()

        super().__init__(**data)

    ADDRESS: Optional[str] = Field(default=None, serialization_alias='address')
    FACILITY: Optional[EnumLogFacilityCode] = Field(default=None, serialization_alias='facility')
    SOCKTYPE: Optional[EnumLogSocketType] = Field(default=None, serialization_alias='socktype')


class StreamHandler(BaseModel):
    def __init__(self, **data: Any):
        should_be_lower_list = ("stream",)
        for i in should_be_lower_list:
            if i in data:
                data[i] = data[i].lower()

        super().__init__(**data)

    STREAM: Optional[EnumLogStream] = Field(default=None, serialization_alias='stream')


class SchemaLogging(BaseModel):
    def __init__(self, **data: Any):
        should_be_upper_list = ("LEVEL",)
        for i in should_be_upper_list:
            if i in data:
                data[i] = data[i].upper()

        should_be_lower_list = ("HANDLERS",)
        for i in should_be_lower_list:
            if i in data:
                if isinstance(data[i], str):
                    data[i] = data[i].lower()

        if 'HANDLERS' in data:
            if isinstance(data['HANDLERS'], str):
                values = data['HANDLERS'] \
                    .replace('[', "") \
                    .replace(']', "") \
                    .replace('"', "") \
                    .strip() \
                    .split(",")

                values = [i.strip() for i in values]
                for i in values:
                    if i not in EnumLogHandler._value2member_map_:
                        raise ValueError(f"{i} is not in EnumLogHandler!")

                data['HANDLERS'] = values

        super().__init__(**data)

    NAME: str = Field(serialization_alias='name')
    LEVEL: EnumLogLevel = Field(serialization_alias='level')
    HANDLERS: list[EnumLogHandler] = Field(serialization_alias='handlers')
    FORMAT: str = Field(serialization_alias='format_')

    TIMED_ROTATING_FILE_HANDLER: TimedRotatingFileHandler = Field(
        default=None,
        serialization_alias='timed_rotating_file_handler',
    )
    SYSLOG_HANDLER: SysLogHandler = Field(
        default=None,
        serialization_alias='syslog_handler',
    )
    STREAM_HANDLER: StreamHandler = Field(
        default=None,
        serialization_alias='stream_handler',
    )
