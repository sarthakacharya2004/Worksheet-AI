def deep_flatten(lst):
    """
    Flattens a deeply nested list into a single list.
    Parameters: lst (list): A deeply nested list
    Returns: list: A single flattened list
    """
    result = []
    for item in lst:
        if type(item) == list:
            flattened = deep_flatten(item)
            for element in flattened:
                result.append(element)
        else:
            result.append(item)
    return result

my_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(deep_flatten(my_list))