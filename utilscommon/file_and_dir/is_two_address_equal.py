from pathlib import Path


def is_two_address_equal(address_a, address_b):
    if address_a == address_b:
        return True

    path_address_a = Path(address_a).resolve()
    path_address_b = Path(address_b).resolve()

    if path_address_a == path_address_b:
        return True
    return False


if __name__ == "__main__":
    print(is_two_address_equal("/home/ragham/Desktop/programming/ir_scratcher/utils_common/is_two_address_equal.py",
                               "./is_two_address_equal.py"))
