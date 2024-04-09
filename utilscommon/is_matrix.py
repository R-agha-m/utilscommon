from os.path import exists
from os import getenv
from platform import system


def is_matrix():
    os_type = system().lower()
    if os_type.startswith('win'):
        return False

    proc_1 = r'/proc/1/sched'

    if exists(proc_1):
        with open(proc_1, 'r') as fp:
            out = fp.read()
    else:
        out = ''

    checks = ['docker' in out,
              '/lxc/' in out,
              out.split(' ')[0] not in ('systemd', 'init',),
              exists('./dockerenv'),
              exists('/.dockerinit'),
              getenv('container') is not None]

    return any(checks)
