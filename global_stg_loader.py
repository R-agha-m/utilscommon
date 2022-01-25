from os import environ
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path

try:
    from .is_two_address_equal import is_two_address_equal
except ImportError:
    from is_two_address_equal import is_two_address_equal


def global_stg_loader(current_stg_address,
                      stg_class_name="LocalStg", ):
    STG_MODULE_ADDRESS = environ.get("STG_MODULE_ADDRESS")
    if (not STG_MODULE_ADDRESS) or is_two_address_equal(STG_MODULE_ADDRESS, current_stg_address):
        class GlobalStg:
            pass
    else:
        module_name = Path(STG_MODULE_ADDRESS).name
        spec = spec_from_file_location(module_name, STG_MODULE_ADDRESS)
        global_stg_module = module_from_spec(spec)
        spec.loader.exec_module(global_stg_module)
        GlobalStg = getattr(global_stg_module, stg_class_name)

    return GlobalStg
