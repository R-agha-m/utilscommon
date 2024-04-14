class ProjectBaseException(Exception):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self,
                    key,
                    value)

#                         code: int,
#             success: bool = None,
#             data: None | dict | list = None,
#             error: str | dict | list | None = None,
#             message: str | dict | list | None = None,
#             log_this_exc: bool = False


class PathCannotBeFound(ProjectBaseException):
    pass


class CannotGetIPAddress(ProjectBaseException):
    pass


class NetworkError(ProjectBaseException):
    pass


class UnacceptableOpenMode(ProjectBaseException):
    pass


class Fail2OpenFile(ProjectBaseException):
    pass


class CannotCheckProxy(ProjectBaseException):
    pass


class IPFound(ProjectBaseException):
    pass


class FakeException4Test(Exception):
    pass


class IsOnly4Test(Exception):
    pass
