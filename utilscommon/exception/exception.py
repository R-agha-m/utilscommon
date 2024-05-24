from .project_base_exception import ProjectBaseException


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
