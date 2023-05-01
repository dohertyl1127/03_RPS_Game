import random


# functions go here
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

        return response


# Main routine goes here
rounds_played = 0
choose_instruction = "please choose rock (r), paper (p), or scissors (s)"

# ask for # of rounds, <enter> for infinite mode
rounds = check_rounds()

mode = "regular"

end_game = "no"
while end_game == "no":
    print()
    if rounds == "":
        mode = "infinite"
        rounds = 5

    elif mode == "infinite":
        heading = f"continuous mode: round {rounds_played + 1}"
        rounds += 1

    else:
        heading = f"round {rounds_played + 1} of {rounds}"
    print(heading)
    choose = input(f"{choose_instruction}" 
                   " or 'xxx' to end: ")

    if choose == "xxx":
        break

    # rest of loop / game
    print(f"you choose {choose}")

    rounds_played += 1

    if rounds_played <= rounds:
        break

print("thank you for playing")
