def flatten(lst):
    """
    Flattens a nested list into a single list.
    Parameters: lst (list): A nested list
    Returns: list: A flattened single list
    """
    print(lst)
    result = []
    for inner_list in lst:
        for item in inner_list:
            result.append(item)
    return result

my_list = [[1, 2], [3, 4], [5]]
print(flatten(my_list))