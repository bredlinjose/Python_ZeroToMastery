def extract_data_based_on_the_key1(dict1: dict, key):
    res = []

    if key in dict1:
        res.append(dict1[key])
    for outer_key in dict1:
        inner_keys = dict1[outer_key]

        if key in inner_keys:
            value = inner_keys[key]
            res.append(value)

    return res


def extract_data_based_on_the_key2(dict1: dict, key):
    result = []

    # First check in the top-level dictionary
    if key in dict1:
        result.append(dict1[key])

    # Then check in the nested dictionaries
    for value in dict1.values():
        if isinstance(value, dict) and key in value:
            result.append(value[key])

    return result


if __name__ == "__main__":
    dict1 = {
        "Gfg": {"a": 100, "b": 200, "c": 300},
        "Ran": {"a": "abc", "b": "efg", "c": "hij"},
        "Dem": {"a": True, "c": False},
        "c": "Data"
    }
    key = "c"
    output1 = extract_data_based_on_the_key1(dict1, key)
    print(output1)

    output2 = extract_data_based_on_the_key2(dict1, key)
    print(output2)
