def get_last_n(numbers, n):
    """
    Extracts the last n elements from a list.
    Parameters: lst (list): A list of elements, n (int): Number of elements to extract
    Returns: list: A list containing the last n elements
    """
    print(numbers)
    result = []
    for i in range(len(numbers) - n, len(numbers)):
        result.append(numbers[i])
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_last_n(my_list, 2))