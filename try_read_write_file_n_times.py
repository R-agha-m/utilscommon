from .exception import UnacceptableOpenMode, Fail2OpenFile, PathCannotBeFound
from time import sleep
from traceback import format_exc
import stg
from os.path import exists


def try_read_write_file_n_times(path,
                                mode='r',
                                data_2_write=None,
                                n=None,
                                raise_if_fails=True):
    n = n or stg.MAX_TRY
    
    if not exists(path):
        raise PathCannotBeFound

    for i in range(1, n + 1):
        try:
            with open(path, mode, encoding='utf-8') as handler:
                if mode == 'r':
                    return handler.read()
                elif mode in {'w', 'a'}:
                    return handler.write(data_2_write)
                else:
                    raise UnacceptableOpenMode
        except UnacceptableOpenMode as e:
            raise e
        except Exception:
            if raise_if_fails and (i == n):
                raise Fail2OpenFile

            stg.report.warning(format_exc())
            sleep(stg.POLL_FREQUENCY)
