print("Welcome to the secret auction program!!")

# Dictionary to store bidder names and their bid amounts
bids_dictionary = {}

# Flag to control the loop
last_bidder = False

def clear_screen():
    # Clears the screen (here we simulate it with newlines)
    print("\n" * 20)

def get_bid_input():
    # Collects input from one bidder
    name = input("Enter your name: ")
    amount = int(input("Enter your bidding amount: ₹"))
    return name, amount

def ask_last_bidder():
    # Checks if this is the last bidder
    response = input("Are you the last bidder? Type 'yes' or 'no': ").lower()
    return response == "yes"

def find_highest_bidder(bids):
    # Finds the highest bidder from the dictionary
    highest_bid = 0
    winner = ""
    for name, amount in bids.items():
        if amount > highest_bid:
            highest_bid = amount
            winner = name
    return winner, highest_bid

# Main loop to collect bids
while not last_bidder:
    clear_screen()
    name, amount = get_bid_input()
    bids_dictionary[name] = amount
    last_bidder = ask_last_bidder()

# Determine the winner
winner_name, highest_amount = find_highest_bidder(bids_dictionary)
print(f"\n🎉 {winner_name} won the auction with a bid of ₹{highest_amount}!")
