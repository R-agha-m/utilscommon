from datetime import (
    datetime,
    timedelta,
)
from os.path import exists


class GenerateBuildVersioning:
    def __init__(
            self,
            build_file_address: str,
            version: str,
    ):
        self.build_file_address = build_file_address
        self.version = version

        self.build_version = None
        self.build_datetime_str = None
        self.build_datetime = None
        self.need_to_write = False
        self.data = None

    def perform(self):
        self.read_file()
        self.extract_build_version()
        self.manage_new_build_version()
        self.write_file()
        return f"{self.version}.{self.build_version}.{self.build_datetime_str}"

    def read_file(self):
        if exists(self.build_file_address):
            with open(self.build_file_address, 'r') as handler:
                self.data = handler.read()
        else:
            self.data = None

    def extract_build_version(self):
        build_version = None
        build_datetime_str = None
        need_to_write = False

        if self.data:
            split_value = self.data.split(".")
            build_version = int(split_value[0])

            if len(split_value) == 1:
                build_datetime_str = datetime.utcnow().strftime('%Y%m%d%H%M')
                need_to_write = True

            elif len(split_value) == 2:
                build_datetime_str = split_value[-1]

        if build_version is None:
            build_version = 1
            build_datetime_str = build_datetime_str or datetime.utcnow().strftime('%Y%m%d%H%M')

            need_to_write = True

        self.build_version = build_version
        self.build_datetime_str = build_datetime_str
        self.build_datetime = datetime.strptime(build_datetime_str, '%Y%m%d%H%M')
        self.need_to_write = need_to_write

    def manage_new_build_version(self):
        if datetime.utcnow() > (self.build_datetime + timedelta(minutes=60)):
            self.build_version += 1
            self.build_datetime_str = datetime.utcnow().strftime('%Y%m%d%H%M')

            self.need_to_write = True

    def write_file(self):
        if self.need_to_write:
            with open(self.build_file_address, 'w') as handler:
                handler.write(f"{self.build_version}.{self.build_datetime_str}")


def generate_build_versioning(
        build_file_address: str,
        version: str,
):
    return GenerateBuildVersioning(
        build_file_address=build_file_address,
        version=version,
    ).perform()
