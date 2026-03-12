def get_first_n(numbers, n):
    """
    Extracts the first n elements from a list.
    Parameters: lst (list): A list of elements, n (int): Number of elements to extract
    Returns: list: A list containing the first n elements
    """
    print(numbers)
    result = []
    for i in range(n):
        result.append(numbers[i])
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_first_n(my_list, 3))