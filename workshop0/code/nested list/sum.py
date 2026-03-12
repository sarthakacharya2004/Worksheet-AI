def sum_nested(lst):
    """
    Calculates the sum of all elements in a nested list.
    Parameters: lst (list): A nested list
    Returns: int/float: Sum of all elements in the nested list
    """
    total = 0
    for item in lst:
        if type(item) == list:
            total = total + sum_nested(item)
        else:
            total = total + item
    return total

my_list = [[1, 2], [3, [4, 5]], 6]
print(sum_nested(my_list))