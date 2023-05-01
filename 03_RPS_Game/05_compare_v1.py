rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    user_choice = rps_list[user_index]
    comp_choice = rps_list[comp_index]
    user_index += 1

    if user_choice == comp_choice:
        result = "tie"

    elif user_choice == "rock" and comp_choice == "scissors":
        result = "win"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "win"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "win"
    else:
        result = "loss"
    print(f"you choose {user_choice}, the computer chooses {comp_choice}. Result: {result}")

    comp_index += 1
    print()
