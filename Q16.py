
score_a = 0
score_b = 0

wins = {
    "stone": "scissor",
    "scissor": "paper",
    "paper": "stone"
}

while score_a < 5 and score_b < 5:
    a = input("Player A: ").lower()
    b = input("Player B: ").lower()

    if a == b:
        print("DRAW")
    elif wins.get(a) == b:
        score_a += 1
        print("Player A wins")
    else:
        score_b += 1
        print("Player B wins")
