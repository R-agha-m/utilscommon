from packaging import version
from pydantic import BaseModel, VERSION
from json import dumps

if version.parse(VERSION) < version.parse("2.0.0"):
    def get_data(value: BaseModel) -> dict:
        """
        Get the dictionary representation of a Pydantic BaseModel object.

        This function converts a Pydantic BaseModel object into a dictionary representation
        by calling its `dict()` method.

        Args:
          value (BaseModel): The Pydantic BaseModel object to convert.

        Returns:
          dict: The dictionary representation of the BaseModel object.

        """
        return value.dict()

elif version.parse(VERSION) >= version.parse("2.0.0"):
    def get_data(value: BaseModel):
        """
        Get the model dump of a Pydantic BaseModel object.

        This function returns the model dump of a Pydantic BaseModel object by calling its
        `model_dump()` method.

        Args:
            value (BaseModel): The Pydantic BaseModel object.

        Returns:
            ModelDump: The model dump of the BaseModel object.

        """
        return value.model_dump()


class Config:
    def __str__(self) -> str:
        """
        Get the string representation of the Config object.

        This method returns a string representation of the Config object. It converts the
        object's attributes and their values into a JSON-like format, including the schema
        and values of each attribute. If an attribute is an instance of Pydantic BaseModel,
        its values are converted using the `get_data()` function.

        Returns:
            str: The string representation of the Config object.

        """
        repr_dict = dict()
        for key, value in self.__dict__.items():
            repr_dict[key] = {
                "schema": str(value.__class__).replace("<class '", "").replace("'>", ""),
                "values": value
            }
            if isinstance(value, BaseModel):
                repr_dict[key]['values'] = get_data(value=value)

        return dumps(repr_dict,
                     sort_keys=False,
                     indent=4
                     )
