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


def choice_checker(question, valid_list, error):
    while True:

        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item
        print(error)


# Main routine goes here

# lists of valid responses
yn_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# ask for # of rounds, <enter> for infinite mode
rounds = check_rounds()

mode = "regular"

end_game = "no"
while end_game == "no":
    print()
    if rounds == "":
        mode = "infinite"
        rounds = 5

    if mode == "infinite":
        heading = f"continuous mode: round {rounds_played + 1}"
        rounds += 1

    else:
        heading = f"round {rounds_played + 1} of {rounds}"

    print(heading)
    choose_instruction = "choose rock / paper / scissors (r/p/s): "
    choose_error = "please choose rock (r), paper (p), or scissors (s)"
    choose = choice_checker(choose_instruction, rps_list,
                            choose_error)

    comp_choice = random.choice(rps_list[:-1])
    print()
    print(f"Comp Choice: {comp_choice}")
    if choose == "xxx":
        break

    # rest of loop / game
    print()
    print(f"you choose {choose}")

    if choose == comp_choice:
        result = "tie"
        rounds_drawn += 1
    elif choose == "rock" and comp_choice == "scissors":
        result = "won"
    elif choose == "paper" and comp_choice == "rock":
        result = "won"
    elif choose == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "loss"
        rounds_lost += 1

    if result == "tie":
        feedback = "its a tie"
    else:
        feedback = f"{choose} vs {comp_choice} - you {result}"

    print()
    print("result: ", result)

    rounds_played += 1

    if rounds_played >= rounds:
        break

# print games stats
rounds_won = rounds_played - rounds_lost - rounds_drawn

print()
print("****End Game Summary****")
print(f"won: {rounds_won} \t|\t  lost: {rounds_lost} \t|\t drawn: {rounds_drawn}")

print()
print("thanks for playing")