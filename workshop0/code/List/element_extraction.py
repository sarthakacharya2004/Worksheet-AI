def extract_element(numbers):
    """
        Extracts every other element from a list starting from the first element.
        Parameters: lst (list): A list of elements
        Returns: list: A new list with every other element
        """
    print(numbers)
    result = []
    for i in range (0, len(numbers), 2):
        result.append(numbers[i])
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(extract_element(my_list))