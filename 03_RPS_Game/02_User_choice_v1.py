# functions go here
def choice_checker(question):

    while True:

        error = "Please chose from rock / paper / scissors (r/p/s) or xxx to quit "
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
    user_choice = choice_checker("choose rock / paper / scissors (r/p/s): ")

    # print out choice for comparison purposes
    print(f"you choose {user_choice}")
