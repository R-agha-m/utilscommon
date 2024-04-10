from os import sep

from configloader.loader import ConfigLoader
from configloader.utils import PrepareLogger, enum, schema, base_dir_path_finder


def test_prepare_logger():
    BASE_DIR_PATH = base_dir_path_finder(
        file_path=__file__,
        number_of_going_up=2
    )

    BASE_DIR_STR = str(BASE_DIR_PATH)

    config_loader = ConfigLoader(
        configs_dir=BASE_DIR_STR + sep + "configs",
        active_section_schemas={
            "LOGGING": schema.Logging,
        },

        raised_on_duplicate_sections=False,
        raised_on_unused_sections=False,
        raised_on_missed_sections=True,

        convert_to_orm_mode=True,
    )

    CONFIG = config_loader.perform()

    prepare_logger_obj = PrepareLogger(
        name=CONFIG.LOGGING.name,
        level=CONFIG.LOGGING.level,
        handlers=CONFIG.LOGGING.handlers,

        format_='{"time":"%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", '
                '"function": "%(funcName)s", "message": "%(message)s"}',

        timed_rotating_file_handler_input={
            "filename": BASE_DIR_STR + sep + "logs" + sep + CONFIG.LOGGING.filename,
            "when": CONFIG.LOGGING.when,
            "interval": CONFIG.LOGGING.interval,
            "backupCount": CONFIG.LOGGING.backupCount,
            "encoding": CONFIG.LOGGING.encoding,
            "delay": CONFIG.LOGGING.delay,
            "utc": CONFIG.LOGGING.utc,
            "atTime": CONFIG.LOGGING.atTime,
            "errors": CONFIG.LOGGING.errors,
        },
        sys_log_handler=None,
        stream_handler=None,
    )
    LOGGER = prepare_logger_obj.perform()

    LOGGER.info("INFO LOGGER")

