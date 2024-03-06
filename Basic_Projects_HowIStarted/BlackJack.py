############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]        #our deck

def start_game():
    return input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  
def draw():
    """Automatically draws from our deck,"""
    return random.choice(cards)

def hand(hand, card):
    """Automatically appends to our hand, 
    and finds our score"""
    hand.append(card)
    return sum(hand)

def aces(hand, score):
    """check how many aces you have and convert the player's
    hand and score automatically"""
    aces = hand.count(11)
    while score > 21 and aces > 0:
        hand[hand.index(11)] = 1  # Change the first ace to 1
        aces -= 1
        score = sum(hand)
    return score, hand  # Return adjusted score and hand

def blackjack():
    while start_game() == "y":    
        from blackjack_art import logo
        print (logo)

        player_cards = []
        while len(player_cards) < 2:                          
            player_score = hand(player_cards, draw())
        if player_score == 22:
            player_cards[1] = 1
            player_score = player_score - 10
   
        computer_cards = []
        computer_score = 0                                   
        while computer_score <= 17:
            computer_score = hand(computer_cards, draw())  # Get a card
            computer_score, computer_cards = aces(computer_cards, computer_score)  # Adjust for aces
            if computer_score > 17:
                break
         
        print (f"Your cards: {player_cards}, current score: {player_score}")
        print (f"Computer's first card: {computer_cards[0]}")

        while player_score <= 21:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()                
            if choice == "n":
                break
            elif choice == "y":
                player_score = hand(player_cards, draw())  # Assign score directly
                player_score, player_cards = aces(player_cards, player_score)
                #player_score = hand(player_cards, draw())
                #aces(player_cards, player_score)
                
                print (f"Your cards: {player_cards}, current score: {player_score}")
                print (f"Computer's first card: {computer_cards[0]}")
            else:
                print ("Invalid choice")
        
        print (f"Your final hand: {player_cards}, final score: {player_score}")
        print (f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        
        if player_score > 21:
            print ("You went over. You lose 😤")
        else:
            
            if computer_score > 21:
                print("You win 😃")
            elif player_score > computer_score:
                print("You win 😃")
            elif player_score == computer_score:
                print("Draw 🙃")
            else:
                print ("You lose!")
    if start_game() == "n":
        print ("Thank you for Playing!")
    #else:
        print ("Invalid Choice")
        start_game()
                
blackjack()
