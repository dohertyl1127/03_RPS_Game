import random


# functions go here
def check_rounds():
    while True:
        response = input("how many rounds? ")

        round_error = "please type either <enter>" \
                      "or an integer that is more than 0"

        if response != "":
            try:

                if int(response) < 1:
                    print(round_error)
                    continue

                else:
                    return response

            except ValueError:
                print(round_error)
                continue


# Main routine goes here
rounds_played = 0
choose_instruction = "please choose rock (r), paper (p), or scissors (s)"

# ask for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":
    print()
    if rounds == "":
        heading = "continuous mode:" / f"round {rounds_played + 1}"

    else:
        heading = f"round {rounds_played + 1} of {rounds}"
    print(heading)
    choose = input(f"{choose_instruction} or 'xxx' to end: ")

    if choose == "xxx":
        break
        
    # rest of loop / game
    print(f"you choose {choose}")

    rounds_played += 1

print("thank you for playing")
