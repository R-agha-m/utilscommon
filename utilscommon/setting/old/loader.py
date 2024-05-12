"""
The `ConfigLoader` class is used to process configuration files and apply corresponding schemas to the active sections.
Here are the extended docstrings for each method:

1. `__init__(self, configs_dir: str, active_section_schemas: Dict[str, Type[BaseModel]],
    raised_on_duplicate_sections: bool = False, raised_on_unused_sections: bool = False,
    raised_on_missed_sections: bool = False, convert_to_orm_mode: bool = False) -> None`:
   - Initializes a new instance of the `ConfigLoader` class.
   - Parameters:
     - `configs_dir`: The directory path where the configuration files are located.
     - `active_section_schemas`: A dictionary mapping section names to their corresponding schema classes.
     - `raised_on_duplicate_sections`: Optional. A boolean indicating whether to raise a `ValueError` if a duplicate
        section is detected. Defaults to `False`.
     - `raised_on_unused_sections`: Optional. A boolean indicating whether to raise a `ValueError` if there is an
        unused section in the configuration file. Defaults to `False`.
     - `raised_on_missed_sections`: Optional. A boolean indicating whether to raise a `ValueError` if a section marked
        as active does not have a corresponding schema. Defaults to `False`.
     - `convert_to_orm_mode`: Optional. A boolean indicating whether to convert the parsed sections to the `Config`
        object in ORM mode. Defaults to `False`.

2. `_extract_config_files_paths(self) -> List[str]`:
   - Extracts the paths of the configuration files from the specified `configs_dir`.
   - Returns a list of configuration file paths.

3. `_read_config_file(self, file_path: str) -> Dict[str, Dict[str, str]]`:
   - Reads the specified configuration file and returns its contents as a dictionary.
   - Parameters:
     - `file_path`: The path of the configuration file to read.
   - Returns a dictionary representing the configuration file contents, with section names as keys and their
   respective options and values as inner dictionaries.

4. `_apply_schema_on_active_sections(self, config_data: Dict[str, Dict[str, str]]) -> Dict[str, Type[BaseModel]]`:
   - Applies the corresponding schema classes on the active sections of the configuration data.
   - Parameters:
     - `config_data`: The dictionary representing the configuration file contents.
   - Returns a dictionary mapping section names to their corresponding schema instances.

5. `_check_4_untouched_sections(self, config_data: Dict[str, Dict[str, str]]) -> None`:
   - Checks for any sections in the configuration file that were not processed or touched by the schema application.
   - Parameters:
     - `config_data`: The dictionary representing the configuration file contents.
   - Raises a `ValueError` if an unused section is detected and `raised_on_unused_sections` is `True`.

6. `_convert_to_orm_mode(self, parsed_sections: Dict[str, Type[BaseModel]]) -> Config`:
   - Converts the parsed sections dictionary to the `Config` object in ORM mode.
   - Parameters:
     - `parsed_sections`: The dictionary mapping section names to their corresponding schema instances.
   - Returns an instance of the `Config` class representing the parsed sections in ORM mode.

7. `perform(self) -> Union[Dict[str, Type[BaseModel]], Config]`:
   - Initiates the processing of configuration files and applies schemas to active sections.
   - Returns either the parsed sections dictionary or the `Config` object, depending on the value of `convert_to_orm_mode`.

8. `get_config(self, section_name: str) -> Type[BaseModel]`:
   - Retrieves the corresponding schema instance for the specified section name from the parsed sections dictionary.
   - Parameters:
     - `section_name`: The name of the section to retrieve the schema for.
   - Returns the schema instance for the specified section name.
"""
from os.path import join
from glob import glob
from configparser import ConfigParser
from typing import Dict, List, Type
from pydantic import BaseModel
from .config_class import Config


class ConfigLoader:
    """
    The ConfigLoader class is used to process configuration files and apply corresponding schemas to the active
    sections. The perform method is called to initiate the processing, and it returns a dictionary mapping section names
    to their corresponding schema instances or the Config object.

    The ConfigLoader class has the following attributes:
    - configs_dir: The directory path where the configuration files are located.
    - active_section_schemas: A dictionary mapping section names to their corresponding schema classes.
    - raised_on_duplicate_sections: A boolean indicating whether to raise a ValueError if a duplicate section is
      detected.
    - raised_on_unused_sections: A boolean indicating whether to raise a ValueError if there is an unused section in
      the configuration file.
    - raised_on_missed_sections: A boolean indicating whether to raise a ValueError if a section marked as active does
      not have a corresponding section in config files.
    - convert_to_orm_mode: A boolean indicating whether to convert the parsed sections from dict to the Config object
      in which section can be access in ORM mode.

    The perform method performs the following operations:
    1. Extracts the paths of the configuration files using the _extract_config_files_paths method.
    2. Iterates over each configuration file path and performs the following operations:
       - Reads the configuration file using the _read_config_file method.
       - Applies the schema on active sections using the _apply_schema_on_active_sections method.
    3. Checks for any untouched sections using the _check_4_untouched_sections method.
    4. If convert_to_orm_mode is True, converts the parsed sections from dict to the Config object using the
       _convert_to_orm_mode method and returns the Config object. Otherwise, returns the parsed sections dictionary.

    The class also provides a get_config method that takes a section name as input and returns the corresponding
    schema instance from the parsed_sections dictionary.

    The class requires the following imports:
    - join from os.path
    - glob from glob
    - ConfigParser from configparser
    - Dict, List, and Type from typing
    - BaseModel from pydantic
    - Config from .config_class
    """

    def __init__(
            self,
            configs_dir: str,
            active_section_schemas: Dict[str, Type[BaseModel]],

            raised_on_duplicate_sections: bool = False,
            raised_on_unused_sections: bool = False,
            raised_on_missed_sections: bool = False,

            convert_to_orm_mode: bool = True,
    ) -> None:
        """
        The __init__ method is the constructor for a class. It initializes the object with the provided input
        parameters.

        Parameters:
        - configs_dir (str): The directory where the configuration files are located.
        - active_section_schemas (Dict[str, Type[BaseModel]]): A dictionary mapping section names to their
          corresponding schema classes.

        Optional Parameters:
        - raised_on_duplicate_sections (bool): If set to True, raises a ValueError if a duplicate section is detected.
          Defaults to False.
        - raised_on_unused_sections (bool): If set to True, raises a ValueError if there is an unused section in the
          configuration file. Defaults to False.
        - raised_on_missed_sections (bool): If set to True, raises a ValueError if a section marked as active does not
          have a corresponding schema. Defaults to False.
        - convert_to_orm_mode (bool): If set to True, converts the configuration to ORM mode. Defaults to True.

        The method assigns the input parameters to the corresponding instance variables of the object.
        """
        self.config_dir = configs_dir
        self.active_section_schemas = active_section_schemas

        self.raised_on_duplicate_sections = raised_on_duplicate_sections
        self.raised_on_unused_sections = raised_on_unused_sections
        self.raised_on_missed_sections = raised_on_missed_sections

        self.convert_to_orm_mode = convert_to_orm_mode

        self.parsed_sections: Dict = dict()
        self.current_config_file_path: str = "/"
        self.raw_config: ConfigParser | None = None
        self.config: Config = Config()

    def perform(self) -> dict[str, BaseModel] | Config:
        """
        Performs the necessary operations to process the configuration files.

        Returns:
            A dictionary mapping section names to their corresponding schema instances or the Config object.

        Raises:
            ValueError: If raised_on_duplicate_sections is True and a duplicate section is detected.
            ValueError: If raised_on_unused_sections is True and there is an unused section in the configuration file.
            ValueError: If raised_on_missed_sections is True and a section marked as active does not have a
            corresponding schema.
        """

        for self.current_config_file_path in self._extract_config_files_paths():
            self._read_config_file()
            self._apply_schema_on_active_sections()

        self._check_for_untouched_sections()

        if self.convert_to_orm_mode:
            self._convert_to_orm_mode()
            return self.config
        else:
            return self.parsed_sections

    def _extract_config_files_paths(self) -> List:
        """
        Extracts the paths of the configuration files from the specified config_dir directory.

        Returns a list of paths to the configuration files in the config_dir directory with the file extension ".cfg".
        """
        # TODO: This docstring should be updated!
        paths = glob(join(self.config_dir, "*.cfg"))
        if not paths:
            raise ValueError(f"No config files are detected!")
        return paths

    def _read_config_file(self) -> None:
        """
        The _read_config_file function is a method that is used to read the configuration files located in the
        specified config_dir directory. The function expects no arguments and does not return any value.

        Within the function, a ConfigParser object is created and assigned to the self.raw_config attribute. This
        object is used to parse and handle the configuration files.

        The read method of the ConfigParser object is then called with the self.current_config_file_path as an
        argument. This method reads and parses the configuration file specified by the path.

        Overall, the purpose of this function is to read the content of a specific configuration file and store it in
        the self.raw_config attribute for further processing or usage within the class.
        """
        self.raw_config = ConfigParser()
        self.raw_config.read(self.current_config_file_path)

    def _apply_schema_on_active_sections(self) -> None:
        """
        The _apply_schema_on_active_sections function is used to apply a schema on the active sections of the
        configuration file.

        The function iterates over each section in the self.raw_config attribute. If the section is present in the
        self.active_section_schemas dictionary, the function checks if the section has already been parsed. If
        self.raised_on_duplicate_sections is set to True, a ValueError is raised indicating that a duplicate section
        has been detected. If the section is not a duplicate, the function retrieves the schema for that section from
        the self.active_section_schemas dictionary. It then retrieves the inputs for that section from the
        self.raw_config object and creates an instance of the schema using the inputs. The instance is then stored in
        the self.parsed_sections dictionary with the section name as the key.

        If the section is not present in the self.active_section_schemas dictionary, and self.raised_on_unused_sections
        is set to True, a ValueError is raised indicating that there is an unused section in the configuration file.

        Overall, the purpose of this function is to apply a schema on the active sections of the configuration file
        and store the parsed sections in the self.parsed_sections attribute for further processing or usage within
        the class.

        :return:
        :rtype:
        """
        # TODO: This docstring should be updated!
        for section in self.raw_config.sections():
            if section in self.active_section_schemas:
                if section in self.parsed_sections:
                    if self.raised_on_duplicate_sections:
                        raise ValueError(f"Duplicate section '{section}' detected!")

                schema = self.active_section_schemas[section]
                inputs = dict(**self.raw_config[section])
                inputs = self._clean_inputs(inputs=inputs)
                self.parsed_sections[section] = schema(**inputs)

            else:
                if self.raised_on_unused_sections:
                    raise ValueError(f"There is unused section '{section}' in {self.current_config_file_path}!")

    @staticmethod
    def _clean_inputs(inputs: dict) -> dict:
        # TODO: This docstring should be updated!
        cleaned_inputs = dict()
        for key, value in inputs.items():
            cleaned_value = value.strip()
            if cleaned_value:
                cleaned_inputs[key] = cleaned_value
        return cleaned_inputs

    def _check_for_untouched_sections(self):
        """
        This method, `_check_for_untouched_sections`, is used to compare the desired configurations with the
        parsed configurations and identify any missing sections. It takes no arguments other than `self`.

        The method starts by creating two sets: `desired_configs` and `parsed_configs`. The `desired_configs` set
        contains the keys of the active section schemas, while the `parsed_configs` set contains the keys of the
        parsed sections.

        Next, it calculates the missing sections by finding the difference between `desired_configs` and
        `parsed_configs` using the `.difference()` method. If there are any missing sections, it enters a conditional
        statement.

        Inside the conditional statement, it first checks if `self.raised_on_missed_sections` is True. If it is, it
        raises a ValueError with a message indicating which config sections are missed in config files. The message
        is constructed by concatenating the string 'These config sections are missed in config files: ' with a
        string representation of `missing_sections`.

        If there are no missing sections or if `self.raised_on_missed_sections` is False, then no exception is raised
        and the method completes without any further actions.

        Note that this code assumes that both `active_section_schemas` and `parsed_sections` are dictionaries where
        keys represent configuration section names.
        """
        desired_configs = set(self.active_section_schemas.keys())
        parsed_configs = set(self.parsed_sections.keys())
        missing_sections = desired_configs.difference(parsed_configs)
        if missing_sections:
            if self.raised_on_missed_sections:
                raise ValueError('These config sections are missed in config files: ' + str(missing_sections))

    def _convert_to_orm_mode(self):
        """
        This method Converts the parsed sections of the configuration into object-relational mapping (ORM) mode. It
        iterates through each key-value pair in the `parsed_sections` dictionary and sets the corresponding attribute
        on the `config` object using the `setattr()` function. This allows for easy mapping of configuration values to
        ORM models.

        Parameters:

        Returns:
            None
        """
        # TODO: Add annotation
        for key, value in self.parsed_sections.items():
            setattr(self.config, key, value)

    def get_config(self, section: str):
        """
        Retrieves the configuration information for a given section.

        Parameters:
            - section (str): The name of the section to retrieve configuration from.

        Returns:
            - Any: The configuration information for the specified section.

        This method is used to retrieve configuration information from a parsed_sections dictionary. It takes a
        'section' parameter, which is a string representing the name of the section to retrieve configuration from.
        The method returns the configuration information associated with that section.
        """
        return self.parsed_sections.get(section)
