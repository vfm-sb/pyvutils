

def is_nested_list(lst: list) -> bool:
    """
    Check if a list contains any nested lists.

    Args:
    lst (list): The list to be checked.

    Returns:
    bool: True if there are nested lists, False otherwise.
    """
    return any(isinstance(item, list) for item in lst)
