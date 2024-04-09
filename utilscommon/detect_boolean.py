
FALSE_STRINGS = {"false", "fals", "0", "", "none"}
TRUE_STRINGS = {"true", "tru", "1"}


def detect_boolean(value):
    if type(value) is str:
        if value.lower() in FALSE_STRINGS:
            return False
        else:
            return True

    else:
        return bool(value)
