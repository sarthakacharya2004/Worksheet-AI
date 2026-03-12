def reverse_list(numbers):
    """
    Reverses a list using slicing.
    Parameters: lst (list): A list of elements
    Returns: list: A reversed list
    """
    print(numbers)
    result = []
    for i in range(len(numbers) - 1, -1, -1):
        result.append(numbers[i])
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse_list(my_list))