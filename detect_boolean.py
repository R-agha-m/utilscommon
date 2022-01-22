def detect_boolean(value):
    if type(value) is str:
        if value.lower() in {"false", "fals", "0", "", "none", }:
            return False
        else:
            return True

    else:
        return bool(value)
