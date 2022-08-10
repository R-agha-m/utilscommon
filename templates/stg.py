from sys import path as sys_path
from pathlib import Path
from os import environ, pathsep, sep
from utils_common.create_dir import create_dir
from utils_common.read_file_or_create_it import read_file_or_create_it


class Setting:
    # ===================================================================================================== directories
    _base_dir = None

    @property
    def BASE_DIR(self):
        if self._base_dir is None:
            self._base_dir = str(Path(__file__).resolve().parent)

            if self._base_dir not in sys_path:
                sys_path.append(self._base_dir)

            if "PYTHONPATH" not in environ:
                environ["PYTHONPATH"] = ''

            if self._base_dir not in environ["PYTHONPATH"]:
                environ["PYTHONPATH"] += pathsep + self._base_dir
        return self._base_dir

    _io_dir = None

    @property
    def IO_DIR(self):
        if self._io_dir is None:
            self._io_dir = create_dir(f"{self.BASE_DIR}{sep}io")
        return self._io_dir

    _output_dir = None

    @property
    def OUTPUT_DIR(self):
        if self._output_dir is None:
            self._output_dir = create_dir(f"{self.IO_DIR}{sep}output_dir")
        return self._output_dir

    # ===================================================================================================== files
    _list_of_sources_file_address = None

    @property
    def LIST_OF_SOURCES_FILE_ADDRESS(self):
        if self._list_of_sources_file_address is None:
            self._list_of_sources_file_address = f"{self.IO_DIR}{sep}list_of_sources.txt"
        return self._list_of_sources_file_address

    _list_of_extracted_sources_file_address = None

    @property
    def LIST_OF_EXTRACTED_SOURCES_FILE_ADDRESS(self):
        if self._list_of_extracted_sources_file_address is None:
            self._list_of_extracted_sources_file_address = f"{self.IO_DIR}{sep}list_of_extracted_sources.txt"
        return self._list_of_extracted_sources_file_address

    # =================================================================================================== io data
    _list_of_sources = None

    @property
    def LIST_OF_SOURCES(self):
        if self._list_of_sources is None:
            from utils_common.clean_str_2_list import clean_str_2_list

            data = read_file_or_create_it(self.LIST_OF_SOURCES_FILE_ADDRESS,
                                          raise_if_not_exist=True)

            self._list_of_sources = clean_str_2_list(data,
                                                     raise_if_empty=True)

        return self._list_of_sources

    _list_of_extracted_sources = None

    @property
    def LIST_OF_EXTRACTED_SOURCES(self):
        if self._list_of_extracted_sources is None:
            from utils_common.clean_str_2_list import clean_str_2_list

            data = read_file_or_create_it(self.LIST_OF_EXTRACTED_SOURCES_FILE_ADDRESS,
                                          raise_if_not_exist=False)

            self._list_of_extracted_sources = set(clean_str_2_list(data,
                                                                   raise_if_empty=False))

        return self._list_of_extracted_sources

    # ===================================================================================================== loggers
    _debug_mode = None

    @property
    def DEBUG_MODE(self):
        if self._debug_mode is None:
            from utils_common.detect_boolean import detect_boolean
            self._debug_mode = detect_boolean(
                environ.get("DEBUG_MODE",
                            False))
        return self._debug_mode

    _report = None

    @property
    def report(self):
        if self._report is None:
            from utils_logging.get_or_create_logger import get_or_create_logger
            self._report = get_or_create_logger(
                destinations=("console", f"{self.IO_DIR}{sep}{self.CONTAINER_NAME}_reports.log"),
                level=10 if self.DEBUG_MODE else 20
            )
        return self._report

    _malreport = None

    @property
    def malreport(self):
        if self._malreport is None:
            from utils_logging.get_or_create_logger import get_or_create_logger
            self._malreport = get_or_create_logger(
                name='malreport',
                destinations=("console", f"{self.IO_DIR}{sep}{self.CONTAINER_NAME}_malreports.log"),
                level=30 if self.DEBUG_MODE else 10
            )
        return self._malreport

    # ===================================================================================================== system
    _os_type = None

    @property
    def OS_TYPE(self):
        if self._os_type is None:
            from platform import system
            self._os_type = system().lower()
        return self._os_type

    _is_matrix = None

    @property
    def IS_MATRIX(self):
        if self._is_matrix is None:
            from utils_common.matrix_checker import is_matrix
            self._is_matrix = is_matrix()
        return self._is_matrix

    _ip = None

    @property
    def IP(self):
        if self._ip is None:
            from utils_common.get_public_ip import GetPublicIp
            self._ip = GetPublicIp().perform()
        return self._ip

    _container_name = None

    @property
    def CONTAINER_NAME(self):
        if self._container_name is None:
            self._container_name = environ.get("CONTAINER_NAME",
                                               "localhost")
        return self._container_name

    _app_name = None

    @property
    def APP_NAME(self):
        if self._app_name is None:
            self._app_name = environ.get("APP_NAME",
                                         "word_extractor")
        return self._app_name

    # ===================================================================================================== workflow
    @property
    def TIME_OUT(self):
        return 5

    @property
    def MAX_TRY(self):
        return 10

    @property
    def FREQUENCY(self):
        return 0.1

    @property
    def IMPLICIT_WAIT_TIME(self):
        return 1

    @property
    def COMMENT_SIGN(self):
        return "#"

    # ===================================================================================================== parameters
    @property
    def VOCABULARY_REGEX_PATTERN(self):
        return r"[a-zA-Z-]{3,}"

    @property
    def OUTPUT_FILE_EXTENSION(self):
        return "weo"  # word extractor output


STG = Setting()
report = STG.report
malreport = STG.malreport
