# functions go here
def choice_checker(question):

    while True:
        response = input(question)

        if response.lower() == "r" or response == "rock":
            return response


# Main routine goes here

# ask users for choice and check if its valid
user_choice = choice_checker("choose rock / paper / scissors (r/p/s): ")

# print out choice for comparison purposes
