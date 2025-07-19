alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '%', '^', '&', '*', '=', '/', '<', '>', '|']

alphabets_no = int(input("Enter the number of letters you need in your password: "))
numbers_no = int(input("Enter the number of nos you need in your password: "))
symbols_no = int(input("Enter the number of symbols you need in your password: "))

import random
pass_list = []

for letters in range(0, alphabets_no):
    pass_list.append(random.choice(alphabets))

for digits in range(0, numbers_no):
    pass_list.append(str(random.choice(numbers)))

for syms in range(0, symbols_no):
    pass_list.append(random.choice(symbols))

#random.shuffle(pass_list) #found this simple way to shuffle instead of doing it manually like below
print(pass_list)
print("".join(pass_list))

#part2 manually done below
scram_pass_list = []
totalchar = alphabets_no + numbers_no + symbols_no

for item in range(0, totalchar):
    chosen_index = random.randint(0, totalchar-1)
    scram_pass_list.append(pass_list[chosen_index])
    del pass_list[chosen_index]
    totalchar -= 1

#print(scram_pass_list)
password1 = "".join(scram_pass_list)
print(f"\nYour Password is: {password1}\n")


'''
HOW I DID:
    1. Problem was to create a password generator, scrambled with letters, numbers, symbols
    2. Initially, got the number of chars needed in each and using that number, chars from each list were chosen using
       for loops with the range and random.choice()
    3. 

    

Here are the key lessons and concepts you've learned and used in your password generator program:

1. Lists
You created and used lists (alphabets, numbers, symbols, pass_list, scram_pass_list) to store and manage groups of characters.

2. User Input
You used input() to get numbers from the user for how many letters, numbers, and symbols to include in the password.

3. Type Conversion
You converted user input from string to integer using int().

4. For Loops
You used for loops with range() to repeat actions (like picking random characters) a specific number of times.

5. Random Module
You imported and used the random module:
random.choice() to pick a random item from a list.
random.randint() to pick a random index for manual shuffling.
(You also learned about random.shuffle() for in-place shuffling.)

6. List Methods
You used append() to add items to a list.
You used del and pop() to remove items from a list.

7. String Methods
You used "".join(list) to convert a list of characters into a string (the final password).

8. Manual Shuffling
You practiced shuffling a list manually by randomly picking and removing items, building a new scrambled list.

9. Printing and Debugging
You used print() to display lists and strings for debugging and output.

10. Comments and Documentation
You wrote comments and a docstring to explain your code and thought process.

How you used them:
You combined all these concepts to take user input, build a list of random characters, 
shuffle them (both with a built-in method and manually), and output a secure, randomized password.

'''
