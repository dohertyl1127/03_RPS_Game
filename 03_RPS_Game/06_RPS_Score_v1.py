rounds_played = 0
rounds_lost = 0
rounds_drawn = 0
test_results = ["won", "won", "loss", "loss", "tie"]

for item in test_results:
    rounds_played += 1

    result = item

    if result == "tie":
        result = "its a tie"
        rounds_drawn += 1
    elif result == "loss":
        result = "its a loss"
        rounds_lost += 1

rounds_won = rounds_played - rounds_lost - rounds_drawn

print()
print("****End Game Summary****")
print(f"won: {rounds_won} lost: {rounds_lost} drawn: {rounds_drawn}")

print()
print("thanks for playing")
