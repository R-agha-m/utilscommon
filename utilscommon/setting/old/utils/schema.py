from packaging import version
from datetime import time
from typing import Optional, Any

from pydantic import VERSION, BaseModel
from . import enum

if version.parse(VERSION) < version.parse("2.0.0"):
    from pydantic import validator

elif version.parse(VERSION) >= version.parse("2.0.0"):
    from pydantic import field_validator as validator

CONVERT_TO_NONE_VALUES = {
    "none",
    "null",
}


class SchemaBaseModel(BaseModel):

    def __init__(self, **data: Any) -> None:
        for key, value in data.copy().items():
            if value.lower() in CONVERT_TO_NONE_VALUES:
                data[key] = None

        super().__init__(**data)


class General(SchemaBaseModel):
    """
    Configuration model for general application settings.

    This class represents the general configuration settings for an application. It defines
    the required attributes for an application, such as whether it is in production mode,
    the application name and description, and the application version.

    Attributes:
        is_production (bool): Indicates whether the application is in production mode.
        application_name (str): The name of the application.
        application_description (str): A description of the application.
        application_version (str): The version of the application.

    Raises:
        None

    """
    is_production: bool
    application_name: str
    application_description: str
    application_version: str


class ServiceAuthentication(SchemaBaseModel):
    hash_salt: Optional[str] = None
    hash_method_name: str


class UvicornServer(SchemaBaseModel):
    """
    Configuration model for the Uvicorn server settings.

    This class represents the configuration settings for the Uvicorn server. It defines
    the required attributes for running the Uvicorn server, such as the application to
    run, the host and port on which to listen, the log level, proxy headers, etc.

    Attributes:
        app (str): The application to run.
        host (str): The host on which the server should listen.
        port (int): The port on which the server should listen.
        log_level (EnumLogLevel): The log level for the server.
        proxy_headers (bool): Indicates whether to respect proxy headers.
        forwarded_allow_ips (str): IP addresses to trust for proxy headers.
        reload (bool): Indicates whether to enable auto-reloading.
        loop (str): The event loop implementation to use.
        workers (int): The number of worker processes to spawn.

    Raises:
        None

    """

    # TODO: This docstring should be updated.
    def __init__(self, **data: Any):
        should_be_upper_list = ("log_level",)
        for i in should_be_upper_list:
            if i in data:
                data[i] = data[i].upper()

        super().__init__(**data)

    app: str
    host: str
    port: int
    log_level: enum.EnumLogLevel
    proxy_headers: bool
    forwarded_allow_ips: str
    reload: bool
    loop: str
    workers: int


class Logging(SchemaBaseModel):
    """
    Configuration model for logging settings.

    This class represents the configuration settings for logging. It defines the
    attributes related to logging, such as the log name, host, port, directory name,
    file name, retention count, and log handlers for both production and development
    environments.

    Attributes:
        name (str): The name of the log.
        host (str | None): The host for logging (optional).
        port (int | None | str): The port for logging (optional).
        directory_name (str): The directory name for log files.
        file_name (str): The file name for log files.
        retention_count (int): The number of log files to retain.
        handlers (str): The comma-separated list of log handlers.
        production_level (EnumLogLevel): The log level for production environment.
        development_level (EnumLogLevel): The log level for development environment.

    Raises:
        ValueError: If an invalid log handler is provided.

    """

    # TODO: This docstring should be updated.

    def __init__(self, **data: Any):
        should_be_upper_list = (
            "level",
            "when",
            "facility",
            "socktype",
        )
        for i in should_be_upper_list:
            if i in data:
                data[i] = data[i].upper()

        should_be_lower_list = (
            "handlers",
            "stream",
        )
        for i in should_be_lower_list:
            if i in data:
                data[i] = data[i].lower()

        super().__init__(**data)

    name: str
    level: enum.EnumLogLevel
    handlers: str

    # Inputs of TimedRotatingFileHandler
    filename: Optional[str] = None
    when: Optional[enum.EnumLogRotatingWhen] = None
    interval: Optional[int] = None
    backup_count: Optional[int] = None
    encoding: Optional[str] = None
    delay: Optional[bool] = None
    utc: Optional[bool] = None
    atTime: Optional[time] = None
    errors: Optional[str] = None

    # Inputs of SysLogHandler
    address_host: Optional[str] = None
    address_port: Optional[int] = None
    facility: Optional[enum.EnumLogFacilityCode] = None
    socktype: Optional[enum.EnumLogSocketType] = None

    # Inputs of StreamHandler
    stream: Optional[enum.EnumLogStream] = None

    @validator("handlers")  # noqa
    def check_handlers(cls, value):
        """
        Validator to check if the provided log handlers are valid.

        This validator ensures that the log handlers provided in the `handlers` attribute
        are valid by splitting the string and checking each handler against the available
        log handlers from the `EnumLogHandler` enumeration.

        Args:
            value (str): The comma-separated string of log handlers.

        Returns:
            List[str]: The list of valid log handlers.

        Raises:
            ValueError: If an invalid log handler is provided.

        """
        values = value.split(",")
        values = [i.strip() for i in values]
        for i in values:
            if i not in enum.EnumLogHandler._value2member_map_:
                raise ValueError(f"{i} is not in EnumLogHandler!")
        return values


class Database(SchemaBaseModel):
    """
    Configuration model for database settings.

    This class represents the configuration settings for the database. It defines the
    attributes for the host, port, database name, username, and password required to
    establish a database connection.

    Attributes:
        host (str): The host of the database server.
        port (int): The port number on which the database server is listening.
        database (str): The name of the database to connect to.
        username (str): The username for authenticating the database connection.
        password (str): The password for authenticating the database connection.

    Raises:
        None

    """
    host: str
    port: int
    database: str
    username: Optional[str]
    password: Optional[str]


class DatabaseWithAuthDb(SchemaBaseModel):
    host: str
    port: int
    database: str
    username: Optional[str] = None
    password: Optional[str] = None
    authdb: Optional[str] = None


class Pagination(SchemaBaseModel):
    """
    Configuration model for pagination settings.

    This class represents the configuration settings for pagination. It defines the
    attribute for the page size, which determines the number of items to display on
    each page when implementing pagination.

    Attributes:
        page_size (int): The number of items to display per page.

    Raises:
        None

    """
    page_size: int


class S3(SchemaBaseModel):
    """
    Configuration model for Amazon S3 settings.

    This class represents the configuration settings for Amazon S3. It defines the
    attributes required for connecting and interacting with an S3 bucket, such as
    the endpoint URL, AWS access key ID, AWS secret access key, signature version,
    region name, bucket name, folder name, and server address.

    Attributes:
        endpoint_url (str): The URL of the S3 endpoint.
        aws_access_key_id (str): The AWS access key ID.
        aws_secret_access_key (str): The AWS secret access key.
        signature_version (str): The signature version for authentication.
        region_name (str): The AWS region name.
        bucket_name (str): The name of the S3 bucket.
        folder_name (str): The name of the folder within the S3 bucket.
        server_address (str): The server address for accessing the S3 bucket.

    Raises:
        None

    """
    endpoint_url: str
    aws_access_key_id: str
    aws_secret_access_key: str
    signature_version: str
    region_name: str
    bucket_name: str
    folder_name: str
    server_address: str


class Emta(SchemaBaseModel):
    """
    Configuration model for Emta settings.

    This class represents the configuration settings for Emta. It defines the
    attributes required for authenticating and interacting with an Emta service,
    such as the URL, API URL, client ID, client secret, and callback URL.

    Attributes:
        url (str): The URL for the Emta service.
        api_url (str): The API URL for the Emta service.
        client_id (str): The client ID for authentication.
        client_secret (str): The client secret for authentication.
        callback_url (str): The callback URL for authentication.

    Raises:
        None

    """
    url: str
    api_url: str
    client_id: str
    client_secret: str
    callback_url: str


class Api(SchemaBaseModel):
    """
    Represents an API configuration.

    This class serves as a model for storing API configuration settings, including the
    API path and API key.

    Attributes:
        path (str): The path or URL of the API.
        api_key (str): The API key used for authentication or access control.

    """
    path: str
    api_key: str


class Token(SchemaBaseModel):
    """
    Represents a token configuration for authentication.

    This class serves as a model for storing token configuration settings, including the
    validity period, algorithm, and secret key used for token generation and validation.

    Attributes:
        validity_period_in_days (int): The validity period of the token in minutes.
        algorithm (str): The algorithm used for token generation and validation.
        secret_key (str): The secret key used for signing and verifying the token.

    """
    validity_period_in_days: int
    algorithm: str
    secret_key: str
    header_key_name: str


class Otp(SchemaBaseModel):
    # TODO: add docstring
    resend_lock_duration_in_second: int
    validity_period_in_second: int
    number_of_characters: int
    allowed_characters: str


class GZipMiddleware(SchemaBaseModel):
    # TODO: add docstring
    minimum_size_in_byte: int
