from platform import system
from os.path import join
from pathlib import Path

try:
    from .run_command import run_command
except ImportError:
    from run_command import run_command


class VenvPreparer:
    def __init__(self,
                 name='venv',
                 base=None,
                 report_func=print):
        self.name = name
        self.base = base if base else str(Path(__file__).resolve().parent.parent)
        self.report_func = report_func

        self.report_func(f"base: {self.base}")

        self.base_and_name = join(self.base,
                                  self.name)
        self.report_func(f"base_and_name: {self.base_and_name}")

        self.shell = True if system().lower().startswith("win") else False
        self.venv_python_address = join(self.base_and_name,
                                        "scripts",
                                        "python.exe")

    def perform(self):
        self._create_venv()
        self._install_requirements()
        self._create_runner_file()

    def _create_venv(self):
        self.report_func(run_command(command=['python',
                                   "-m",
                                   'venv',
                                   f'{self.base_and_name}'],
                          raise_error=True,
                          shell=self.shell))

        self.report_func("venv is created successfully.")

    def _install_requirements(self):
        self.report_func(run_command(command=[self.venv_python_address,
                                   "-m",
                                   "pip",
                                   "install",
                                   '-r',
                                   f'{join(self.base, "requirements.txt")}'],
                          raise_error=True,
                          shell=self.shell))

        self.report_func("requirements is installed successfully.")

    def _create_runner_file(self):
        if system().lower().startswith("win"):
            with open(f"{join(self.base, '__main__.cmd')}", 'w') as handler:
                handler.write(f"\"{self.venv_python_address}\" .")

            self.report_func("runner file is created successfully.")


if __name__ == "__main__":
    VenvPreparer(name="venv").perform()
