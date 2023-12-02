low = 0
high = 996

def ask_for_int(low, high):


    # ask the user for an integer
    while True:

        try:
            user_choice = int(input("Choose an integer between 0 and 996: "))
            if user_choice < low or user_choice > high:
                print("That is outside of the accepted range of integers. Choose again.")
            else:
                return user_choice
        except ValueError:
            print("\n""That is not a valid choice.  Choose again.")

    # use exception handling to check is valid int

    # if valid in check to see if within range of low/high

    # if not in range print an error message

    # return valid integer user entered

    # return user_choice


def factorial(num):

    if num == 0:
        return 1

    return num * factorial(num - 1)


def main():

    print("Hello! Welcome to Today's Lesson." "\n")

    while True:
        loop_again = "Y"

        # call ask_for_int to get an int from user
        user_input = ask_for_int(low, high)

        # call factorial and pass in integer from ask_for_int
        result = factorial(user_input)

        print("Your result is: ", result)

        # ask the user if they want to loop again

        try_again = input("Do you want to try again?  Choose Y or N: ").upper()

        # if yes, loop again, if no break
        if try_again == loop_again:
            continue
        else:
            print("Thank you for participating.  Goodbye")
            break
        # print goodbye message

main()
