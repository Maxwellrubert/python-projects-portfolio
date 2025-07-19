from gamedataforgame import insta_data
from random import choice

def val_pop():
    value = choice(insta_data)              #choice is the library function random.choice(list)
    insta_data.remove(value)
    return value

def display(value1, value2):
    print(f"\nCompare A: {value1['name']}, {value1['description']}, {value1['country']}")
    print("VS")
    print(f"With B: {value2['name']}, {value2['description']}, {value2['country']}\n")

def game():
    print("WELCOME TO HIGHER LOWER GAME!")
    game_over = False
    value1 = val_pop()                      #value3 = insta_data.pop(choice(insta_data))
    score = 0

    while not game_over:
        value2 = val_pop()
        display(value1, value2)
        max_followers = max(value1["followers"], value2["followers"])
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if player_choice == 'a':
            player_value = value1
        elif player_choice == 'b':
            player_value = value2
        else:
            print("Invalid Choice!")
            continue

        if player_value["followers"] != max_followers:
            print(f"Sorry that's wrong, your final score: {score}")
            game_over = True
        elif player_value["followers"] == max_followers:
            score += 1
            print(f"You're right! Your current score: {score}")
            value1 = value2
        else:
            print("Game Error")
            return 0
        
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        game()
    else:
        return 0

game()
