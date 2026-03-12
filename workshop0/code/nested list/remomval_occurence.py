def remove_element(lst, elem):
    """
    Removes all occurrences of a specific element from a nested list.
    Parameters: lst (list): A nested list, elem: Element to remove
    Returns: list: A nested list with the element removed
    """
    result = []
    for inner_list in lst:
        new_inner = []
        for item in inner_list:
            if item != elem:
                new_inner.append(item)
        result.append(new_inner)
    return result

my_list = [[1, 2], [3, 2], [4, 5]]
print(remove_element(my_list, 2))