# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
#USER'S TURN

user_value = draw_starting_hand("YOUR")
while user_value < 21:
  should_hit = input('You have ' + str(user_value) + ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
    user_value += draw_card()
  else:
    print("Sorry I didn't get that.")
print_end_turn_status(user_value)

#DEALER'S TURN
dealer_value = draw_starting_hand("DEALER")
while dealer_value < 17:
  print('Dealer has ' + str(dealer_value) + '.')
  dealer_value += draw_card()
print_end_turn_status(dealer_value)

#GAME RESULT
print_end_game_status(user_value, dealer_value)
