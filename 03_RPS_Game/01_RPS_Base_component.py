import random


# functions go here
def choice_checker(question, valid_list, error):
    while True:

        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item
        print(error)

def check_rounds():
    while True:
        response = input("how many rounds? ")

        round_error = "please type either <enter>" \ 
                      "or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue



# Main routine goes here

# lists of valid responses
yn_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]
# ask users for choice and check if its valid

# print out choice for comparison purposes

