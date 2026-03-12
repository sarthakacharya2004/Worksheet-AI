# This is the file where the conversion question is being solved.

CONV_LENGTH_VALUE = 3.28084
CONV_LENGTH_WEIGHT = 2.20462
CONV_VOLUME_VALUE = 0.26417

def convert_length():
    """
    Convert the length of the converted value to an integer
    :return: float value: The converted value of length
    """
    print("convert length")
    print("1. Meters to Feet")
    print("2. Feet to Meters")

    try:
        user_choice = int(input("Enter your choice: "))
        value = float(input("Enter your value: "))
        if user_choice == 1:
            result = value * CONV_LENGTH_VALUE
            print(f"Your converted value is: {result}")
            return result
        elif user_choice == 2:
            result = value / CONV_LENGTH_VALUE
            print(f"Your converted value is: {result}")
            return result
        else:
            print("Please enter a valid choice")
            return None
    except:
        print("Please enter a valid choice")
        return None


def convert_weight():
    """
    Convert the weight of the converted value to an integer
    :return: float value: The converted value of weight
    """
    print("Weight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")

    try:
        user_choice = input("Enter 1 or 2: ")
        value = float(input("Enter the value to convert: "))

        if user_choice == "1":
            result = value * CONV_LENGTH_WEIGHT
            print(f"{value} kg = {result:.2f} pounds")
            return result
        elif user_choice == "2":
            result = value / CONV_LENGTH_WEIGHT
            print(f"{value} pounds = {result:.2f} kg")
            return result
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return None

    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def convert_volume():
    """
    Converts volume between liters and gallons.
    :return: float value: The converted value of volume
    """
    print("Volume Conversion:")
    print("1. Liters to Gallons")
    print("2. Gallons to Liters")

    try:
        user_choice = input("Enter 1 or 2: ")
        value = float(input("Enter the value to convert: "))

        if user_choice == "1":
            result = value * CONV_VOLUME_VALUE
            print(f"{value} liters = {result:.2f} gallons")
            return result
        elif user_choice == "2":
            result = value / CONV_VOLUME_VALUE
            print(f"{value} gallons = {result:.2f} liters")
            return result
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return None

    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def main():
    """
    Main function that displays the conversion menu
    """
    while True:
        print("1. Length (Meters - Feet)")
        print("2. Weight (Kg - Pounds)")
        print("3. Volume (Liters - Gallons)")
        print("4. Exit")

        try:
            choice = input("\nEnter your choice (1-4): ")

            if choice == "1":
                convert_length()
            elif choice == "2":
                convert_weight()
            elif choice == "3":
                convert_volume()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3 or 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


main()