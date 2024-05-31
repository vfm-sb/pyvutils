"""
List Processors
"""


def remove_duplicates(original_list: list) -> list:
    return list(set(original_list))


def flatten(nested_list: list) -> list:
    flattened_list = []
    for element in nested_list:
        if isinstance(element, list):
            flattened_list.extend(flatten(element))
        else:
            flattened_list.append(element)
    return flattened_list
