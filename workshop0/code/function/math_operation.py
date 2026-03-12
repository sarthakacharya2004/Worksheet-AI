def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers.
    Parameters: numbers (list): A list of numbers
    Returns: float: The sum of all numbers in the list
    """
    total = 0
    for num in numbers:
        total = total + num
    return total


def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Parameters: numbers (list): A list of numbers
    Returns: float: The average of all numbers in the list
    """
    total = 0
    count = 0
    for num in numbers:
        total = total + num
        count = count + 1
    return total / count


def calculate_maximum(numbers):
    """
    Finds the maximum value in a list of numbers.
    Parameters: numbers (list): A list of numbers
    Returns:float: The maximum value in the list
    """
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def calculate_minimum(numbers):
    """
    Finds the minimum value in a list of numbers.
    Parameters: numbers (list): A list of numbers
    Returns:float: The minimum value in the list
    """
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def get_numbers():
    """
    Asks the user to input a list of numbers.
    Returns:list: A list of floating point numbers
    """
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = []
        parts = user_input.split()
        for part in parts:
            converted = float(part)
            numbers.append(converted)

        if len(numbers) == 0:
            print("Error! List cannot be empty.")
            return None

        return numbers

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None


def main():
    """
    Main function that displays the operations menu
    """
    while True:
        print("1. Sum")
        print("2. Average")
        print("3. Maximum")
        print("4. Minimum")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("Goodbye")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please enter 1, 2, 3, 4 or 5.")
            continue

        numbers = get_numbers()

        if numbers is None:
            continue

        if choice == "1":
            result = calculate_sum(numbers)
            print(f"Sum = {result:.2f}")

        elif choice == "2":
            result = calculate_average(numbers)
            print(f"Average = {result:.2f}")

        elif choice == "3":
            result = calculate_maximum(numbers)
            print(f"Maximum = {result:.2f}")

        elif choice == "4":
            result = calculate_minimum(numbers)
            print(f"Minimum = {result:.2f}")

main()