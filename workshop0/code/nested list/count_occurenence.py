def count_occurrences(lst, elem):
    """
    Counts occurrences of a specific element in a nested list.
    Parameters: lst (list): A nested list, elem: Element to count
    Returns: int: Number of times the element appears in the nested list
    """
    count = 0
    for item in lst:
        if type(item) == list:
            count = count + count_occurrences(item, elem)
        else:
            if item == elem:
                count = count + 1
    return count

my_list = [[1, 2], [2, 3], [2, 4]]
print(count_occurrences(my_list, 2))