def find_nth_char_index(string,
                        demand_char='/',
                        occurrence_number=1):
    number = 0
    for i, char in enumerate(string):
        if char == demand_char:
            number += 1
            if number == occurrence_number:
                return i

    return len(string)
