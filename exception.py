class ProjectBaseException(Exception):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self,
                    key,
                    value)


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
