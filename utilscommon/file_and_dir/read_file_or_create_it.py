from os.path import exists


def read_file_or_create_it(
        file_address: str,
        raise_if_not_exist: bool = False,
        initial_value: str = "",
) -> str:
    if exists(file_address):
        with open(file_address, 'r') as file_handler:
            return file_handler.read()

    else:
        with open(file_address, 'a') as handler:
            handler.write(initial_value)

        if raise_if_not_exist:
            raise ValueError(f'{file_address} was not exist! It is created.')

        return initial_value
