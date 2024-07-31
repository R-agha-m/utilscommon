from time import sleep
from traceback import format_exc
from os.path import exists

try:
    from utilscommon.exception import UnacceptableOpenMode, Fail2OpenFile, PathCannotBeFound
except ImportError:
    from exception import UnacceptableOpenMode, Fail2OpenFile, PathCannotBeFound


def try_read_write_file_n_times(path,
                                mode='r',
                                data_2_write=None,
                                n=1,
                                raise_if_fails=True,
                                encoding='utf-8',
                                report_func=print,
                                sleep_func=sleep,
                                sleep_time_between_each=1):
    
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

            if report_func:
                report_func(format_exc())

            if sleep_func:
                sleep_func(sleep_time_between_each)
