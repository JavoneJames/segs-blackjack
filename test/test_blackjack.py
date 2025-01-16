import unittest
from blackjack import BlackJack

class BlackJackTestCase(unittest.TestCase):

    def setUp(self):
        self.bj = BlackJack()
        self.bj.set_up_game()
    
    """ Given I play a game of blackjack
        When I am dealt my opening hand
        Then I have two cards """
    def test_initial_hand(self):
        self.assertEqual(len(self.bj.player.cards), 2, "Player should have 2 cards")