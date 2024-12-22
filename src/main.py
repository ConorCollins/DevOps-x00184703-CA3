from calculator import add, subtract, multiply, divide

def display_menu():
    """Displays the calculator menu."""
    print(
        "Calculator\n"
        "Available operations:\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n"
        "5. Exit"
    )

def process_choice(choice, num1, num2):
    """Performs the selected operation."""
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    try:
        return operations[choice](num1, num2)
    except KeyError:
        return "Invalid choice"
    except ValueError as e:
        return f"Error: {e}"

def main():
    """Simplified main function."""
    display_menu()
    choice = input("Select operation (1/2/3/4/5): ").strip()

    if choice == '5':
        print("Exiting calculator.")
        return

    if choice not in ('1', '2', '3', '4'):
        print("Invalid input. Please select a valid option.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = process_choice(choice, num1, num2)
        print(f"The result is: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
