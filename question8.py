# Day of the week checker



def get_day_of_week():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Ask the user for input
        try:
        day_number = int(input("Enter a number from 1 to 7: "))

        if 1 <= day_number <= 7:
            print(f"The day corresponding to {day_number} is: {days_of_week[day_number - 1]}")
        else:
            print("Please enter a valid number between 1 and 7.")
        except ValueError:
        print("Invalid input. Please enter a number.")
