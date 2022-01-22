from os import makedirs


def create_dir(address):
    makedirs(address, exist_ok=True)
    return address
