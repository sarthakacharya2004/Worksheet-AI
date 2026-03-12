def remove_first_last(numbers):
    """
    Removes the first and last elements of a list.
    Parameters: lst (list): A list of elements
    Returns: list: A sublist without the first and last elements
    """
    print(numbers)
    result = []
    for i in range(1, len(numbers) - 1):
        result.append(numbers[i])
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_first_last(my_list))