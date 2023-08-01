def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value

if __name__ == "__main__":
    # Get an integer input from the user
    user_input = input("Enter an integer: ")

    try:
        # Convert the input string to an integer
        user_integer = int(user_input)
        factorial_result = factorial(user_integer)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")