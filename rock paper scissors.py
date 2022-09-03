import random
def play():
    user = input("What's your choice?\n'r' for rock, 'p' for paper, 's' for scissors :\n")
    computer = random.choice(["r", "s", "p"])

    if user == computer:
        return "It's a tie"
    if is_win(user, computer):
        return "YOU WON, YAY!!!!!!"
    if is_win(computer, user):
        return "SHIT, YOU LOST"
    # r>s, p>r, s>p
def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") or (player == "s" and opponent == "p"):
        return True
print(play())