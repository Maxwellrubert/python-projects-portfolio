
rock = ''' 
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

bot_choices = [rock, paper, scissors]
bot_choice = random.choice(bot_choices)
player_choice = input("Pick your choice, Type rock or paper or scissors: ").lower()

if player_choice == "paper":
    player_choice = paper

if player_choice == "scissors":
    player_choice = scissors

if player_choice == "rock":
    player_choice = rock


print(f"You Chose: {player_choice}")
print(f"Bot Chose: {bot_choice}")

if player_choice == rock and bot_choice == rock:
    print("Match Draw!")

elif player_choice == rock and bot_choice == paper:
    print("You lose, Bot Wins!")

elif player_choice == rock and bot_choice == scissors:
    print("You Win!!")

elif player_choice == paper and bot_choice == rock:
    print("You Win!!")

elif player_choice == paper and bot_choice == paper:
    print("Match Draw!")

elif player_choice == paper and bot_choice == scissors:
    print("You Lose, Bot Wins!")

elif player_choice == scissors and bot_choice == rock:
    print("You Lose, Bot Wins!")

elif player_choice == scissors and bot_choice == paper:
    print("You Win!")

elif player_choice == scissors and bot_choice == scissors:
    print("Match Draw!")

else:
    print("You lose, pick a proper choice")