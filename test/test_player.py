import unittest
from unittest.mock import MagicMock, patch
from src.player import Player
from src.dealer import Dealer
from src.card import Card


class PlayerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        # create a mock dealer and pass it to the Player
        mock_dealer = MagicMock(Dealer)  # Mock the Dealer class
        self.player = Player(mock_dealer)

        # define the mock cards
        self.card_king = Card('K')
        self.card_ace = Card('A')
        self.card_queen = Card('Q')
        self.card_9 = Card('9')

        # use mock to return the specific cards
        mock_dealer.deal_card.side_effect = [self.card_king, self.card_ace, self.card_queen, self.card_9]

    def tearDown(self):  # this method will be run after each test
        pass

    """ Given my score is updated or evaluated
        When it is 21 or less
        Then I have a valid hand """
    def test_valid_hand_score_less_than_or_equal_21(self):
        self.player.retrieve_card(self.card_king)
        self.player.retrieve_card(self.card_ace)
        self.assertTrue(self.player.score() <= 21)

    """ Given my score is updated
        When it is 22 or more 
        Then I am ‘bust’ and do not have a valid hand """
    def test_bust_hand_score_more_than_21(self):
        self.player.retrieve_card(self.card_king)
        self.player.retrieve_card(self.card_ace)
        self.player.retrieve_card(Card('10'))
        print(f"Player's score after dealing cards: {self.player.score()}")
        self.assertTrue(self.player.score() > 21)
    
    """ Given I have a King and an Ace
        When my score is evaluated
        Then my score is 21 """
    def test_king_and_ace_score(self):
        self.player.retrieve_card(self.card_king)
        self.player.retrieve_card(self.card_ace)
        self.assertEqual(self.player.score(), 21)

    """ Given I have a king, a queen, and an ace
        When my score is evaluated
        Then my score is 21 """
    def test_king_queen_and_ace_score(self):
        self.player.retrieve_card(self.card_king)
        self.player.retrieve_card(self.card_queen)
        self.player.retrieve_card(self.card_ace)
        self.assertEqual(self.player.score(), 21)

    """ Given I have a nine, an ace, and another ace
        When my score is evaluated
        Then my score is 21 """
    def test_9_ace_and_ace_score(self):
        self.player.retrieve_card(self.card_9)
        self.player.retrieve_card(self.card_ace)
        self.player.retrieve_card(self.card_ace)
        self.assertEqual(self.player.score(), 21)
            