from os import environ


def load_parameters(name,
                    can_use_config_file=False,
                    config_file=None,
                    parent_name_in_config_file=None,
                    default=None):

    parameter = environ.get(name)

    if (parameter is None) and can_use_config_file:
        parameter = config_file[parent_name_in_config_file].get(name)

    if not parameter:
        parameter = default

    return parameter
