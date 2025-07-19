import random

print("Welcome to the number guessing game!!")
chosen_number = random.randint(1, 100)

def choose_difficulty():
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if mode == "easy":
        chances = 10
        return chances
    elif mode == "hard":
        chances = 5
        return chances
    else:
        print("Invalid Input!")
        return 0
    
def guess(chances):
    while chances != 0:
        guessed_num = int(input("Make a guess: "))
        if guessed_num == chosen_number:
            print(f"Wow! You've guessed the correct value, which is {guessed_num}, with {chances} chances left")
            return 0
        elif guessed_num > chosen_number:
            print("TOO HIGH\nGuess Again")
            chances -= 1
            print(f"You have {chances} chances left\n")
        elif guessed_num < chosen_number:
            print("TOO LOW\nGuess Again")
            chances -= 1
            print(f"You have {chances} chances left\n")
        else:
            return 0

chances = choose_difficulty()
guess(chances)