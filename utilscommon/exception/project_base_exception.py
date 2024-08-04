class ProjectBaseException(Exception):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(
                self,
                key,
                value,
            )

#             status_code: int,
#             success: bool = None,
#             data: None | dict | list = None,
#             error: str | dict | list | None = None,
#             message: str | dict | list | None = None,
#             log_this_exc: bool = False

    def __str__(self):
        return str({
            self.__class__.__name__: {
                key: str(value) for key, value in self.__dict__.items() \
                if not key.startswith('__') \
                   and not callable(value)
            }
        })
