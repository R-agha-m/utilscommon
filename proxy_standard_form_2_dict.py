def proxy_standard_form_2_dict(raw_proxy,
                               separators=":@:",
                               key_names=("username", "password", "host", "port",)):
    # 'Selyelenasoft:Q1q7PeI@23.26.228.141:45785'

    results = list()
    for raw_proxy_i in raw_proxy:

        prepared_proxy_i = dict()
        for separator_index, separator in enumerate(separators):
            index = raw_proxy_i.find(separator)
            if index < 0:
                raise ValueError(f"'{raw_proxy_i}' has no '{separator}'")

            prepared_proxy_i[key_names[separator_index]] = raw_proxy_i[:index]
            raw_proxy_i = raw_proxy_i[index+1:]

        prepared_proxy_i[key_names[-1]] = raw_proxy_i
        results.append(prepared_proxy_i)

    return results


if __name__ == "__main__":
    result = proxy_standard_form_2_dict(
        raw_proxy=['Selyelenasoft1:Q1q7PeI1@23.26.228.141:45781',
                   'Selyelenasoft2:Q1q7PeI2@23.26.228.142:45782'],
        separators=":@:",
        key_names=("username", "password", "host", "port",)
    )

    print(result)
