from os import environ
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from sys import modules

global_stg_holder = None

try:
    from .is_two_address_equal import is_two_address_equal
except ImportError:
    from is_two_address_equal import is_two_address_equal


def global_stg_loader(current_stg_address,
                      stg_class_name="LocalStg"):

    global global_stg_holder
    if global_stg_holder is not None:
        return global_stg_holder

    STG_MODULE_ADDRESS = environ.get("STG_MODULE_ADDRESS")
    if (not STG_MODULE_ADDRESS) or is_two_address_equal(STG_MODULE_ADDRESS, current_stg_address):
        class GlobalStg:
            pass
        return GlobalStg
    else:
        module_address_path = Path(STG_MODULE_ADDRESS).resolve()
        module_name_with_suffix = module_address_path.name
        module_name_without_suffix = module_address_path.stem
        if module_name_without_suffix not in modules:
            spec = spec_from_file_location(module_name_with_suffix, str(module_address_path))
            global_stg_module = module_from_spec(spec)
            spec.loader.exec_module(global_stg_module)
        else:
            global_stg_module = modules[module_name_without_suffix]

        GlobalStg = getattr(global_stg_module, stg_class_name)
        global_stg_holder = GlobalStg
        return GlobalStg


def register_global_stg(stg_stg_class):
    global global_stg_holder
    if global_stg_holder is None:
        global_stg_holder = stg_stg_class
