def get_sublist(numbers, start, end):
    """
    Returns a sublist from start index to end index (inclusive).
    Parameters: lst (list): A list of elements, start (int): Starting index, end (int): Ending index
    Returns: list: A sublist from start to end
    """
    print(numbers)
    result = []
    for i in range(start, end + 1):
        result.append(numbers[i])
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_sublist(my_list, 2, 4))