import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_card1 = random.choice(cards)
player_card2 = random.choice(cards)

dealer_card1 = random.choice(cards)

player_cards = []
dealer_cards = []

player_cards.append(player_card1)
player_cards.append(player_card2)
dealer_cards.append(dealer_card1)

def display():
    print(f"Your cards: {player_cards}  Your Total Score: {sum(player_cards)}")
    print(f"Dealer Card: {dealer_cards[0]}")

def player_hit():
    player_cards.append(random.choice(cards)) 
    if player_cards[-1] == 11:   #Ace Exception
        if sum(player_cards) > 21:
            player_cards[-1] = 1
    display()

def dealer_hit():
    while sum(dealer_cards) <= 17:
        dealer_cards.append(random.choice(cards))
    print(f"Dealer Card: {dealer_cards} Dealer Total: {sum(dealer_cards)}")

def compare():
    if sum(player_cards) < 21: 
        if sum(dealer_cards) > 21:
            print(f"You win!! Your Score:{sum(player_cards)} | Dealer Score:{sum(dealer_cards)}")
            exit()
        elif sum(player_cards) > sum(dealer_cards):
            print(f"You win!! Your Score:{sum(player_cards)} | Dealer Score:{sum(dealer_cards)}")
            exit()
        elif sum(player_cards) < sum(dealer_cards):
            print(f"Dealer Wins! You lose! Your Score:{sum(player_cards)} | Dealer Score:{sum(dealer_cards)}")
            exit()
        elif sum(player_cards) == sum(dealer_cards):
            print(f"Match Draw! Your Score:{sum(player_cards)} | Dealer Score:{sum(dealer_cards)}")
        else:
            print("Game Error")
    elif sum(player_cards) > 21:
        print(f"Dealer Wins! You lose! Your Score:{sum(player_cards)} | Dealer Score:{sum(dealer_cards)}")
        exit()
    else:
        print("Byee")
    exit()

def blackjack():
    if sum(player_cards) == 21:
        print("Black Jack!! You win!")
        exit()
    elif sum(player_cards) < 21:
        while sum(player_cards) < 21:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == 'y':
                player_hit()
                if sum(player_cards) > 21:
                    dealer_cards.append(random.choice(cards))
                    if dealer_cards[-1] == 11:   #Ace Exception
                        if sum(dealer_cards) > 21:
                            dealer_cards[-1] = 1
                    print(f"Dealer Cards: {dealer_cards}")
                    compare()
            elif choice == 'n':
                dealer_hit()
                compare()
            else:
                print("Invalid choice")
    else:
        print("Game Error")

print("Welcome to Blackjack!")
display()
blackjack()









"""
import random

# Cards list: Aces are 11, face cards are 10
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def deal_card():
    #Returns a random card from the deck
    return random.choice(cards)

def calculate_score(hand):
    #Calculates the score of a hand and handles Ace (11 or 1)
    score = sum(hand)
    if 11 in hand and score > 21:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def show_status(player, dealer, hide_dealer_card=True):
    #Displays the current hands
    print(f"\nYour cards: {player} | Total: {calculate_score(player)}")
    if hide_dealer_card:
        print(f"Dealer's cards: [{dealer[0]}, ?]")
    else:
        print(f"Dealer's cards: {dealer} | Total: {calculate_score(dealer)}")

# Initial deal
player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]

game_over = False

# Check for instant Blackjack
if calculate_score(player_hand) == 21:
    show_status(player_hand, dealer_hand, False)
    print("🎉 Blackjack! You win!")
    game_over = True

# Player's turn
while not game_over:
    show_status(player_hand, dealer_hand)
    choice = input("Type 'y' to hit or 'n' to stand: ").lower()

    if choice == 'y':
        player_hand.append(deal_card())
        if calculate_score(player_hand) > 21:
            show_status(player_hand, dealer_hand, False)
            print("💥 You busted! Dealer wins.")
            game_over = True
    elif choice == 'n':
        game_over = True
    else:
        print("Invalid input. Please type 'y' or 'n'.")

# Dealer's turn
if calculate_score(player_hand) <= 21:
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    show_status(player_hand, dealer_hand, False)

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21:
        print("🎉 Dealer busted! You win!")
    elif dealer_score > player_score:
        print("😓 Dealer wins!")
    elif dealer_score < player_score:
        print("🎉 You win!")
    else:
        print("🤝 It's a draw!")

"""