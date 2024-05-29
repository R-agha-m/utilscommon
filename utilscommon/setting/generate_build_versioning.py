from datetime import date
from os.path import exists


def generate_build_versioning(
        build_file_address: str,
        version: str,
):
    if exists(build_file_address):
        with open(build_file_address, 'r') as handler:
            build_version = handler.read()

        build_version = int(build_version) + 1

    else:
        build_version = 1

    with open(build_file_address, 'w') as handler:
        handler.write(str(build_version))

    datetime_version = date.today().strftime('%Y%m%d')
    build_version = int(build_version/2)
    return f"{version}.{build_version}.{datetime_version}"
