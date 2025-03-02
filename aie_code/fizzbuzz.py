def fizzbuzz(numbers):
    # Type checking
    if numbers is None:
        raise TypeError("Input cannot be None")
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    result = []

    for num in numbers:
        # Check if input is a valid integer
        if not isinstance(num, (int)):
            raise TypeError("All elements must be integers")

        # Convert number to appropriate string based on rules
        if num == 0:
            result.append("FizzBuzz")
        elif num % 15 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))

    return result
