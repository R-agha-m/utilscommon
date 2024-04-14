def line_reader_and_cleaner(
        raw_data: str,
        replace_chars: tuple[tuple[str, str]] = (("\r\n", "\n"),),
        split_chars: tuple[str, ...] = ("\n",),
        elimination_chars: tuple[str, ...] = ("#",),
        eliminate_empty_lines: bool = True,
        strip_space: bool = True,
        make_lower: bool = True,
        make_unique: bool = True,
):
    if replace_chars:
        for char, replace_char in replace_chars:
            raw_data = raw_data.replace(char, replace_char)

    if split_chars:
        raw_data = [raw_data]

        for split_char in split_chars:
            raw_data_new = list()
            for raw_data_i in raw_data:
                raw_data_new.extend(raw_data_i.split(split_char))
            raw_data = raw_data_new

    if elimination_chars:
        for elimination_char in elimination_chars:
            raw_data = [i for i in raw_data if not i.startswith(elimination_char)]

    if strip_space:
        raw_data = [i.strip() for i in raw_data]

    if eliminate_empty_lines:
        raw_data = [i for i in raw_data if i]

    if make_lower:
        raw_data = [i.lower() for i in raw_data]

    if make_unique:
        raw_data = list(set(raw_data))

    return raw_data


if __name__ == "__main__":
    result = line_reader_and_cleaner(raw_data="reza\r\n#naghi\ntaghi\nvahi,ed",
                                     replace_chars=(("\r\n", "\n"),),
                                     split_chars=("\n",),
                                     elimination_chars=("#",),
                                     make_lower=True,
                                     make_unique=True)

    print(result)
