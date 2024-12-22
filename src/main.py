# src/main.py

from calculator import add, subtract, multiply, divide

def main():
    print("Calculator")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        try:
            choice = input("\nSelect operation (1/2/3/4/5): ")
            if choice == '5':
                print("Exiting calculator.")
                break

            if choice not in ('1', '2', '3', '4'):
                print("Invalid input. Please select a valid option.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print(f"The result is: {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"The result is: {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"The result is: {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result is: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
