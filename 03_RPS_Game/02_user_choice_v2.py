# version 2 - error message included when function is called

# functions go here
def choice_checker(question, error):

    while True:

        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response

        elif response == "xxx":
            return response
        else:
            print(error)


# Main routine goes here

# loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    # ask users for choice and check if its valid
    user_choice = choice_checker("choose rock / paper / scissors (r/p/s): ", "Please chose from rock / paper / scissors (r/p/s) or xxx to quit ")

    # print out choice for comparison purposes
    print(f"you choose {user_choice}")
