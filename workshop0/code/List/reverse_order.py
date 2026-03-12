def reverse_skip(numbers):
    """
    Extracts every second element starting from second-to-last moving backward.
    Parameters: lst (list): A list of elements
    Returns: list: A new list with every second element in reverse order
    """
    print(numbers)
    result = []
    for i in range(len(numbers) - 2, -1, -2):
        result.append(numbers[i])
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse_skip(my_list))