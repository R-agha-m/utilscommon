from enum import Enum


class EnumXCase(str, Enum):
    CAMEL_CASE = 'camelCase'
    PASCAL_CASE = 'PascalCase'
    LOWER_SNAKE_CASE = 'lower_snake_case'
    UPPER_SNAKE_CASE = 'UPPER_SNAKE_CASE'
    LOWER_KEBAB_CASE = 'lower-kebab-case'
    UPPER_KEBAB_CASE = 'UPPER-KEBAB-CASE'


def from_case_to_x_case(
        text: str,
        input_case: EnumXCase,
        output_case: EnumXCase,
        separator_char: None | str = None,
        connector_char: None | str = None,
) -> str:
    if input_case == EnumXCase.LOWER_SNAKE_CASE:
        if output_case == EnumXCase.CAMEL_CASE:
            split_text = text.split(separator_char or '_')
            ready_text = [split_text[0]]
            ready_text.extend([i.title() for i in split_text[1:]])
            return f'{connector_char or ""}'.join(ready_text)

        elif output_case == EnumXCase.PASCAL_CASE:
            split_text = text.split(separator_char or '_')
            ready_text = [i.title() for i in split_text]
            return f'{connector_char or ""}'.join(ready_text)
