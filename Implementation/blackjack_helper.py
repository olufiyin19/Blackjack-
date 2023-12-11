# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint
# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

def print_card_name(card_rank):
    # Implement card_name function here
    if card_rank == 1:
    # A 1 stands for an ace.
        card_name = "Ace"
    elif card_rank == 11:
    # An 11 stands for a jack.
        card_name = "Jack"
    elif card_rank == 12:
    # A 12 stands for a queen.
        card_name = "Queen"
    elif card_rank == 13:
    # A 13 stands for a king.
        card_name = "King"
    else:
    # All other cards are named by their number, or rank.
        card_name = str(card_rank)
        #print(card_name)
    if card_rank > 13:
        print("BAD CARD")
    if card_rank == 1 or card_rank == 8:
        print('Drew an ' + card_name)
    else:
        if card_rank <= 13:
            if card_rank != 1 or card_rank != 8: 
                print('Drew a ' + card_name)

def draw_card():
    # Implement draw_card function here
    card_rank = randint(1,13)
    print_card_name(card_rank)
    if card_rank == 11 or card_rank == 12 or card_rank == 13:
    # Jacks, Queens, and Kings are worth 10.
        card_value = 10
    elif card_rank == 1:
    # Aces are worth 11.
        card_value = 11
    else:
    # All other cards are worth the same as their rank.
        card_value = card_rank
    return card_value
  
def print_header(message):
    # Implement print_header function here
    print("-----------")
    print(message)
    print("-----------")

def draw_starting_hand(name):
    # Implement draw_starting_hand function here
    print_header(name.upper() + " TURN")
    card1 = draw_card()
    card2 = draw_card()
    sum = card1 + card2
    return sum

#hand_value = draw_starting_hand("name")
def print_end_turn_status(hand_value):
    # Implement print_end_turn_status function here
    
    if hand_value == 21:
        print("Final hand: {}. \nBLACKJACK!".format(hand_value))
    elif hand_value > 21:
        print("Final hand: {}. \nBUST.".format(hand_value))
    else:
        print("Final hand: {}.".format(hand_value))

def print_end_game_status(user_hand, dealer_hand):
    # Implement print_end_game_status function here
  print_header("GAME RESULT")
  if user_hand <= 21 and dealer_hand > 21:
    print("You win!")
  if user_hand > 21:
    print("Dealer wins!")
  if dealer_hand <= 21 and user_hand <= 21:
    if user_hand > dealer_hand:
      print("You win!")
    elif dealer_hand == user_hand:
      print("Push.")
    else:
      print("Dealer wins!")

