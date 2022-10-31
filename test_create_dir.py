from unittest import TestCase, main
from os.path import exists
from os import rmdir, sep
from pathlib import Path


try:
    from .create_dir import create_dir
except ImportError:
    from create_dir import create_dir


class CreateDirTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.package_address = str(Path(__file__).resolve().parent)

    def test_create_dir_when_dir_is_not_exist(self):
        address = f"{self.package_address}{sep}dir4test"
        try:
            rmdir(address)
        except FileNotFoundError:
            pass
        address = create_dir(address=address)
        self.assertTrue(exists(address))

    def test_create_dir_when_dir_is_exist(self):
        address = f"{self.package_address}{sep}dir4test"
        address = create_dir(address=address)
        address = create_dir(address=address)  # second call assures that the dir is exist
        self.assertTrue(exists(address))


if __name__ == "__main__":
    main()
