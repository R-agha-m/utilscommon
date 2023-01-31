# def handle_none_in_nested_dict(dict_data: dict,
#                                keys: tuple):
#     data = dict_data.copy()
#     for index, key in enumerate(keys, 1):
#         data = data.get(key)
#         if index == len(keys):
#             return data
#
#         elif not isinstance(data, dict):
#             return None

def handle_none_in_nested_dict(dict_data: dict,
                               keys: tuple):
    if len(keys) == 0:
        return dict_data

    elif len(keys) == 1:
        return dict_data.get(keys[0])

    else:
        data = dict_data.get(keys[0])
        if isinstance(data, dict):
            return handle_none_in_nested_dict(dict_data=data,
                                              keys=keys[1:])
        else:
            return data
