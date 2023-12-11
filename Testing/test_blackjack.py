from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_busts_and_user_doesnt(self, input_mock, randint_mock):
        '''
        User receives cards that end up with a hand less than 21 and the
        dealer receives cards that end up with a hand greater than 21
        
        The user wins by having a hand that does not bust.
        '''
        output = run_test([10, 10], ['n'], [5, 9, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 10\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 9\n" \
                   "Dealer has 14.\n" \
                   "Drew a 9\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_blackjacks_and_dealer_busts(self, input_mock, randint_mock):
        '''
        User receives cards that end up with a hand equal to 21 and the
        dealer receives cards that end up with a hand greater than 21
        
        The user wins by having a hand that equals BLACKJACK.
        '''
        output = run_test([2, 3, 13, 6], ['y', 's', 'y'], [12, 4, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 3\n" \
                   "You have 5. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "You have 15. Hit (y/n)? s\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 4\n" \
                   "Dealer has 14.\n" \
                   "Drew an 8\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_blackjacks_and_dealer_doesnt(self, input_mock, randint_mock):
        '''
        User receives cards that end up with a hand equal to 21 and the
        dealer receives cards that end up with a hand less than 21
        
        The user wins by having a hand that equals BLACKJACK.
        '''
        output = run_test([2, 3, 13, 6], ['y', 's', 'y'], [12, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 3\n" \
                   "You have 5. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "You have 15. Hit (y/n)? s\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 9\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_blackjacks_and_dealer_gets_17(self, input_mock, randint_mock):
        '''
        User receives cards that end up with a hand equal to 21 and the
        dealer receives cards that end up with a hand less than 21 that equals 17
        
        The user wins by having a hand that equals BLACKJACK.
        '''
        output = run_test([2, 3, 13, 6], ['y', 'y'], [1, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 3\n" \
                   "You have 5. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 6\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_greater_than_dealer_under_21(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.

        The user wins by having a higher hand than the dealer.
        '''
        output = run_test([1, 9], ['n'], [2, 3, 11, 3], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 9\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 3\n" \
                   "Dealer has 5.\n" \
                   "Drew a Jack\n" \
                   "Dealer has 15.\n" \
                   "Drew a 3\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_busts_and_dealer_doesnt(self, input_mock, randint_mock):
        '''
        User receives cards that end up with a hand greater than 21 and the
        dealer receives cards that end up with a hand less than 21
        
        The dealer wins by having a hand that does not bust.
        '''
        output = run_test([13, 12, 2], ['y'], [10, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a Queen\n" \
                   "You have 20. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew an 8\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_blackjacks_and_user_busts(self, input_mock, randint_mock):
        '''
        User receives cards that end up with a hand greater than 21 and the
        dealer receives cards that end up with a hand equal to 21
        
        The dealer wins by having a hand that equals BLACKJACK.
        '''
        output = run_test([6, 7, 4, 2, 3], ['y', 'v', 'y', 'y'], [13, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 7\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 17. Hit (y/n)? v\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 19. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_blackjacks_and_user_doesnt(self, input_mock, randint_mock):
        '''
        User receives cards that end up with a hand less than 21 and the
        dealer receives cards that end up with a hand equal to 21
        
        The dealer wins by having a hand that equals BLACKJACK.
        '''
        output = run_test([4, 3, 1], ['y', 'n'], [6, 7, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 3\n" \
                   "You have 7. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 7\n" \
                   "Dealer has 13.\n" \
                   "Drew an 8\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_bust_user_greater_than_dealer(self, input_mock, randint_mock):
        '''
        Both the dealer and user both receive cards that end up with a hand greater than 21.

        The dealer wins because the user busts.
        '''
        output = run_test([2, 3, 4, 5, 5, 6], ['y', 'd', 'y', 'y', 'j', 'y'], [6, 7, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 3\n" \
                   "You have 5. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 9. Hit (y/n)? d\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 9. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 19. Hit (y/n)? j\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 19. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 7\n" \
                   "Dealer has 13.\n" \
                   "Drew a 9\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_bust_user_less_than_dealer(self, input_mock, randint_mock):
        '''
        Both the dealer and user both receive cards that end up with a hand greater than 21.

        The dealer wins because the user busts.
        '''
        output = run_test([1, 1], [], [1, 5, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 5\n" \
                   "Dealer has 16.\n" \
                   "Drew a 7\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_bust_user_equal_to_dealer(self, input_mock, randint_mock):
        '''
        Both the dealer and user both receive cards that end up with a hand greater than 21.

        The dealer wins because the user busts.
        '''
        output = run_test([1, 2, 9], ['y'], [1, 2, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 2\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 2\n" \
                   "Dealer has 13.\n" \
                   "Drew a 9\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_under_21_dealer_greater(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.

        The dealer wins by having a higher hand than the user.
        '''
        output = run_test([1, 5, 2], ['y', 'n'], [1, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 5\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 9\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_blackjack(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand equal 21.

        The user pushes because they have a hand value equal to 21 and equal to that of the dealer.
        '''
        output = run_test([2, 3, 4, 5, 7], ['f', 'y', 'y', 'y'], [13, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 3\n" \
                   "You have 5. Hit (y/n)? f\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 5. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 9. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_equal_under_21(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.

        The user pushes because they have a hand value less than 21 and equal to that of the dealer.
        '''
        output = run_test([1, 9], ['n'], [1, 2, 3, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 9\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 2\n" \
                   "Dealer has 13.\n" \
                   "Drew a 3\n" \
                   "Dealer has 16.\n" \
                   "Drew a 4\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
