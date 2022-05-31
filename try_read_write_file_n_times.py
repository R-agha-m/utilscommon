from time import sleep
from traceback import format_exc
from os.path import exists
from stg import STG, report

try:
    from .exception import UnacceptableOpenMode, Fail2OpenFile, PathCannotBeFound
except ImportError:
    from exception import UnacceptableOpenMode, Fail2OpenFile, PathCannotBeFound


def try_read_write_file_n_times(path,
                                mode='r',
                                data_2_write=None,
                                n=STG.MAX_TRY,
                                raise_if_fails=True,
                                encoding='utf-8'):
    
    if (mode == 'r') and (not exists(path)):
        raise PathCannotBeFound

    for i in range(1, n + 1):
        try:
            with open(path, mode, encoding=encoding) as handler:
                if 'r' in mode:
                    return handler.read()

                elif 'w' in mode:
                    return handler.write(data_2_write)

                elif 'a' in mode:
                    return handler.write(data_2_write)
                else:
                    raise UnacceptableOpenMode
        except UnacceptableOpenMode as e:
            raise e
        except Exception:
            if raise_if_fails and (i == n):
                raise Fail2OpenFile

            report.warning(format_exc())
            sleep(STG.POLL_FREQUENCY)
