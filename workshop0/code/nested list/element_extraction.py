def access_nested_element(lst, indices):
    """
    Extracts a specific element from a nested list using indices.
    Parameters: lst (list): A nested list, indices (list): A list of indices
    Returns: element at the given position
    """
    print(lst)
    element = lst
    for index in indices:
        element = element[index]
    return element

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(access_nested_element(my_list, [1, 2]))