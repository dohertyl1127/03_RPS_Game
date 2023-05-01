game_summary = []

rounds_lost = 0
rounds_drawn = 0
rounds_played = 5

for item in range(0, 5):
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
print("***** Game Summary *****")
for game in game_summary:
    print(game)
print()

print("***** Game Statistics *****")
print(f"Winrate: {percent_win}% ")
print(f"loserate: {percent_lose}% ")
print(f"tierate: {percent_tie}% ")
