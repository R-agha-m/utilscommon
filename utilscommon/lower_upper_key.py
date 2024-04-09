

def lower_upper_key(dict_, key, default=None):
    return dict_.get(key.lower()) or dict_.get(key.upper(), default)
