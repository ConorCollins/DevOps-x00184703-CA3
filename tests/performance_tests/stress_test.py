from src.calculator import add, divide

def stress_test():
    try:
        # Test addition with very large numbers
        large_result = add(10**100, 10**100)
        print(f"Stress Test: add(10^100, 10^100) = {large_result}")

        # Test division by zero
        print("Stress Test: Division by zero")
        divide(10, 0)  # This should raise an error
    except ValueError as e:
        print(f"Error during stress test: {e}")

if __name__ == "__main__":
    print("Running Stress Test:")
    stress_test()
