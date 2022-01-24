from os import environ
from importlib.util import spec_from_file_location, module_from_spec


def global_stg_loader(stg_class_name="LocalStg"):
    STG_MODULE_ADDRESS = environ.get("STG_MODULE_ADDRESS")
    if STG_MODULE_ADDRESS:
        from pathlib import Path
        module_name = Path(STG_MODULE_ADDRESS).name
        spec = spec_from_file_location(module_name, STG_MODULE_ADDRESS)
        global_stg_module = module_from_spec(spec)
        spec.loader.exec_module(global_stg_module)
        GlobalStg = getattr(global_stg_module, stg_class_name)
        print(f"Global setting module: {STG_MODULE_ADDRESS}")
    else:
        class GlobalStg:
            pass

        print(f"Package local setting module")

    return GlobalStg
