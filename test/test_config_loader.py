import pytest
from os import sep, environ
from sys import path as sys_path
from utilsconfigloader.loader import ConfigLoader
from utilsconfigloader.utils import schema

try:
    from utilscommon.utilscommon.base_dir_path_finder import base_dir_path_finder
    from utilscommon.utilscommon.add_dir_to_env import add_dir_to_env
except ImportError:
    from utilscommon.base_dir_path_finder import base_dir_path_finder
    from utilscommon.add_dir_to_env import add_dir_to_env


def test_load_config_in_orm_mode():
    base_dir = base_dir_path_finder(
        file_path=__file__,
        number_of_going_up=2
    )

    base_dir = str(base_dir)

    assert base_dir.split(sep=sep)[-1] == "utilsconfigloader", "base_dir is detected wrongly!"

    add_dir_to_env(path_=base_dir)

    assert base_dir in sys_path, "base_dir is not in sys_path"
    assert base_dir in environ["PYTHONPATH"], "base_dir is not in environ['PYTHONPATH']"

    config_loader = ConfigLoader(
        configs_dir=base_dir + sep + "configs",
        active_section_schemas={
            "GENERAL": schema.General,
            "DATABASE": schema.Database,
            "LOGGING": schema.Logging,
            "OTP": schema.Otp,
        },

        raised_on_duplicate_sections=False,
        raised_on_unused_sections=False,
        raised_on_missed_sections=False,

        convert_to_orm_mode=True,
    )

    CONFIG = config_loader.perform()
    attributes = ("GENERAL", "DATABASE")
    for i in attributes:
        assert getattr(CONFIG, i, None), f"CONFIG has not the attribute: {i}"

    print(CONFIG)


def test_load_config_in_dict_mode():
    base_dir = base_dir_path_finder(
        file_path=__file__,
        number_of_going_up=2
    )

    base_dir = str(base_dir)

    config_loader = ConfigLoader(
        configs_dir=base_dir + sep + "configs",
        active_section_schemas={
            "GENERAL": schema.General,
            "DATABASE": schema.Database,
        },

        raised_on_duplicate_sections=False,
        raised_on_unused_sections=False,
        raised_on_missed_sections=False,

        convert_to_orm_mode=False,
    )

    CONFIG = config_loader.perform()
    keys = ("GENERAL", "DATABASE")
    for i in keys:
        assert i in CONFIG, f"CONFIG has not the key: {i}"
        assert config_loader.get_config(i)


def test_load_config_with_raised_on_duplicate_sections():
    base_dir = base_dir_path_finder(
        file_path=__file__,
        number_of_going_up=2
    )

    base_dir = str(base_dir)

    config_loader = ConfigLoader(
        configs_dir=base_dir + sep + "configs",
        active_section_schemas={
            "GENERAL": schema.General,
            "DATABASE": schema.Database,
        },

        raised_on_duplicate_sections=True,
        raised_on_unused_sections=False,
        raised_on_missed_sections=False,

        convert_to_orm_mode=True,
    )

    with pytest.raises(ValueError):
        CONFIG = config_loader.perform()


def test_load_config_with_raised_on_unused_sections():
    base_dir = base_dir_path_finder(
        file_path=__file__,
        number_of_going_up=2
    )

    base_dir = str(base_dir)

    config_loader = ConfigLoader(
        configs_dir=base_dir + sep + "configs",
        active_section_schemas={
            "GENERAL": schema.General,
            "DATABASE": schema.Database,
        },

        raised_on_duplicate_sections=False,
        raised_on_unused_sections=True,
        raised_on_missed_sections=False,

        convert_to_orm_mode=True,
    )

    with pytest.raises(ValueError):
        CONFIG = config_loader.perform()


def test_load_config_with_raised_on_missed_sections():
    base_dir = base_dir_path_finder(
        file_path=__file__,
        number_of_going_up=2
    )

    base_dir = str(base_dir)

    config_loader = ConfigLoader(
        configs_dir=base_dir + sep + "configs",
        active_section_schemas={
            "GENERAL": schema.General,
            "DATABASE": schema.Database,
            "DATABASE33333": schema.Database,
        },

        raised_on_duplicate_sections=False,
        raised_on_unused_sections=False,
        raised_on_missed_sections=True,

        convert_to_orm_mode=True,
    )

    with pytest.raises(ValueError):
        CONFIG = config_loader.perform()
