import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low
        feedback = input(f"Number {computer_guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = computer_guess - 1
        elif feedback == "l":
            low = computer_guess + 1
    print("YAY THE COMPUTER GUESSED YOUR NUMBER, {comuter_guess} , CORRECTLY!")
computer_guess(100)