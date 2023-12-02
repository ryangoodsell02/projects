def ask_for_int(low, high):
    # Use a global variable to avoid re-initializing low and high within the function
    global low, high

    # ask the user for an integer
    while True:
        try:
            user_choice = int(input("Choose an integer between {} and {}: ".format(low, high)))
            if user_choice < low or user_choice > high:
                print("That is outside of the accepted range of integers. Choose again.")
            else:
                return user_choice  # Return the valid user input
        except ValueError:
            print("\n""That is not a valid integer.  Choose again.")


def factorial(num):
    # Use the provided num argument instead of calling ask_for_int again
    if num == 0:
        return 1

    return num * factorial(num - 1)  # Recursively call factorial to calculate the result


def main():
    print("Hello! Welcome to Today's Lesson." "\n")

    while True:
        loop_again = "Y"

        # Get an integer from the user using ask_for_int
        user_input = ask_for_int(0, 996)

        # Calculate the factorial using factorial(user_input)
        result = factorial(user_input)

        print("Your result is: ", result)

        # Ask the user if they want to loop again
        try_again = input("Do you want to try again?  Choose Y or N: ").upper()

        # Break out of the loop if the user chooses N
        if try_again != loop_again:
            print("Thank you for participating.  Goodbye")
            break

        # Continue the loop if the user chooses Y
        else:
            continue

main()