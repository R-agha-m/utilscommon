from sys import argv


def check_4_test_mode() -> bool:
    args = " ".join(argv)
    if "-m unittest" in args:
        return True
    elif "_jb_unittest_runner.py" in args:  # Test is run by pycharm
        return True
    elif len(argv) > 1 and argv[1] == 'test':  # django test
        return True
    return False


def is_test_mode() -> bool:
    return check_4_test_mode()
