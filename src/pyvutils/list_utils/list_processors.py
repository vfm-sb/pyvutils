"""
List Processors
"""


def remove_duplicates(original_list: list) -> list:
    return list(set(original_list))


def flatten_list(nested_list: list) -> list:
    flattened_list = []
    for element in nested_list:
        if isinstance(element, list):
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)
    return flattened_list
