# version 3 - checks that the response is in a given list

# functions go here
def choice_checker(question, valid_list, error):
    while True:

        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item
        print(error)


# Main routine goes here

# list for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]
# loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    # ask users for choice and check if its valid
    user_choice = choice_checker("choose rock / paper / scissors (r/p/s): ", rps_list,
                                 "Please chose from rock / paper / "
                                 "scissors (r/p/s) or xxx to quit ")

    # print out choice for comparison purposes
    print(f"you choose {user_choice}")
