import math
game_summary = []

rounds_lost = 0
rounds_drawn = 0
rounds_played = 3

for item in range(0, 3):
    result = input("choose result: ")

    outcome = f"round {item}: {result}"

    if result == "loss":
        rounds_lost += 1
    elif result == "tie":
        rounds_drawn += 1

    game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost - rounds_drawn

percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("***** Game History *****")
for item in game_summary:
    print(item)

print()

print("***** Game Statistics *****")
print(f"Wins: {rounds_won} ({round(percent_win,2)}%) ")
print(f"loss: {rounds_lost} ({round(percent_lose, 2)}%) ")
print(f"ties: {rounds_drawn} ({round(percent_tie, 2)}%) ")


