def find_max(lst):
    """
    Finds the maximum element in a nested list.
    Parameters: lst (list): A nested list
    Returns: int/float: The maximum element in the nested list
    """
    maximum = None
    for item in lst:
        if type(item) == list:
            current = find_max(item)
        else:
            current = item

        if maximum is None:
            maximum = current
        elif current > maximum:
            maximum = current
    return maximum

my_list = [[1, 2], [3, [4, 5]], 6]
print(find_max(my_list))