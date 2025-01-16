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

    # """ Given I have a valid hand of cards
    #     When I choose to ‘hit’
    #     Then I receive another card
    #     And my score is updated """
    # @patch('builtins.input', side_effect=['h', 's'])
    # def test_player_hit(self, mock_choose_action):
    #     # sim being dealt these cards
    #     self.player.retrieve_card(self.card_ace)
    #     self.player.retrieve_card(self.card_ace)
        
    #     # alc their score
    #     initial_score = self.player.score()
    #     # sim player's turn
    #     self.player.turn()
    #     # check card count has increased and check score after hitting
    #     self.assertGreater(len(self.player.cards), 2, "Player should have more than 2 cards after hitting")
    #     self.assertGreaterEqual(self.player.score(), initial_score, "Player's score should be updated after hitting")

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
        self.assertTrue(self.player.score() > 21)