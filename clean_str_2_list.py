from stg import STG


def clean_str_2_list(data,
                     raise_if_empty=False):
    data = data.replace('\r\n', '\r')
    data = data.split('\n')
    
    clean_data = list()
    for i in data:
        if len(i.replace(" ", '')) > 0:
            if not i.startswith(STG.COMMENT_SIGN):
                clean_data.append(i)

    if (not clean_data) & raise_if_empty:
        raise ValueError('data is empty!')

    return clean_data
