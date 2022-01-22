from .find_nth_char_index import find_nth_char_index
import stg


def clean_url(url, slash_number=2):
    if url.startswith(APARAT_MAIN_ADDRESS):
        url = url.replace(APARAT_MAIN_ADDRESS, '')

    if not url.endswith('/'):
        url += "/"

    index = find_nth_char_index(string=url,
                                demand_char='/',
                                occurrence_number=slash_number)

    return APARAT_MAIN_ADDRESS + url[:index]
