from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return the current date for further use

def calculate_future_date(current_date, days_to_add):
    """
    Calculates and displays the future date after adding a specified number of days.

    Args:
        current_date (datetime): The current date and time.
        days_to_add (int): The number of days to add to the current date.
    """
    future_date = current_date + timedelta(days=days_to_add)  # Add days to the current date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
    print(f"Future date: {formatted_future_date}")
    return future_date  # Return the future date if needed elsewhere

def main():
    # Part 1: Display the current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

if __name__ == "__main__":
    main()
