def safe_divide(numerator, denominator):
    try:
        # Try to convert the input values to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform the division
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        # Handle case where input is not a valid number
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # Handle division by zero error
        return "Error: Cannot divide by zero."
