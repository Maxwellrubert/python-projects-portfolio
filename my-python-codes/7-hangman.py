hangwords = [
    "apple", "banana", "grape", "melon", "peach", "cherry", "orange", "papaya",
    "kiwi", "mango", "carrot", "potato", "tomato", "onion", "garlic", "pepper",
    "coffee", "candle", "puzzle", "window", "bottle", "jacket", "helmet", "pencil",
    "rabbit", "squirrel", "tiger", "zebra", "giraffe", "monkey", "parrot", "falcon",
    "ocean", "forest", "desert", "tunnel", "garden", "castle", "bridge", "shadow"
]

import random

chosen_word = random.choice(hangwords)
print(chosen_word)
chosen_word_as_list = list(chosen_word)
print(chosen_word_as_list)
dashcount = len(chosen_word)
print(dashcount)

dashes = []
for dash in range(dashcount):
    dashes.append("_")
print("Number of letters to be guessed: ")
print("".join(dashes))

replaced_letters_count = 0
lives_count = 6
while replaced_letters_count < dashcount+1 and lives_count != 0:
    if replaced_letters_count == dashcount:
        print("Congratulations! You've found the word by guessing all the letters!\n")
        replaced_letters_count +=1
        break
    if lives_count == 0:
        print("You've lost all the lives\nGAME OVER!!")
        break
    letter_guessed = input("Guess a letter: ")
    if letter_guessed in chosen_word_as_list:
        chosen_letter_index = chosen_word_as_list.index(letter_guessed)
        if dashes[chosen_letter_index] == "_":
            dashes[chosen_letter_index] = letter_guessed
        elif dashes[chosen_letter_index] != "_":
            chosen_letter_index_list = []
            index1 = 0
            for value in chosen_word_as_list:
                if value == letter_guessed:
                    chosen_letter_index_list.append(index1)
                    index1 += 1
                    #break
                elif value != letter_guessed:
                    index1 += 1
                    continue
                else:
                    index1 += 1
                    continue               #not necessary
            for index2 in chosen_letter_index_list:
                #print(chosen_letter_index_list)
                if dashes[index2] != "_":
                    continue
                elif dashes[index2] == "_":
                    dashes[index2] = letter_guessed

        print("Wow! You have the guessed a correct letter!")
        print("".join(dashes))
        print("\n")
        print(f"****************You have {str(lives_count)}/6 lives left****************\n")
        replaced_letters_count += 1
    else: 
        print("Oops! You have guessed a wrong letter!")
        print("".join(dashes))
        lives_count -= 1
        print("\n")
        print(f"****************You have {str(lives_count)}/6 lives left****************\n")


"""
Hangman Program Algorithm
1. Prepare the Word List
Create a list called hangwords containing possible words for the game.

2. Import Modules
Import the random module to help pick a random word.

3. Choose a Word
Randomly select a word from hangwords and store it in chosen_word.
Convert chosen_word into a list of its letters (chosen_word_as_list).
Get the length of the word (dashcount).

4. Set Up the Game Board
Create a list called dashes with the same number of underscores as the letters in the word (to show unguessed letters).

5. Initialize Game Variables
Set replaced_letters_count to 0 (to track how many letters have been guessed).
Set lives_count to 6 (the number of wrong guesses allowed).

6. Main Game Loop
Repeat the following steps while the player still has lives and hasn’t guessed all letters:
Check for Win/Loss:
If replaced_letters_count equals the number of letters, print a win message and break the loop.
If lives_count is 0, print a loss message and break the loop.
Ask for a Guess:
Prompt the player to input a letter (letter_guessed).
Check the Guess:
If the guessed letter is in the word:
Find all positions of that letter in the word.
For each position, if the dash is still "_", replace it with the guessed letter.
Print a success message and the updated dashes.
Increase replaced_letters_count by 1.
If the guessed letter is not in the word:
Print a failure message and the current dashes.
Decrease lives_count by 1.
Show Game Status:
Print the number of lives left.

7. End of Game
After the loop, the game ends with either a win or loss message.


Summary of Concepts Used
Lists: To store words, letters, and dashes.
Random: To pick a word randomly.
Loops: For repeating the guessing process.
Conditionals: To check guesses and game status.
User Input: To get guesses from the player.
String/List Manipulation: To update and display the game board.
"""