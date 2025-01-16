import unittest
from unittest.mock import patch
from src.dealer import Dealer
from src.deck import Deck
from src.card import Card

class PlayerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.dealer = Dealer(self.deck)

    def tearDown(self):  # this method will be run after each test
        pass

    # test if shuffle_deck calls shuffle_deck method
    def test_shuffle_deck(self):
        self.dealer.shuffle_deck()
        self.deck.shuffle_deck.assert_called_once()

    # test if deal_card calls deal_card method and return a card
    def test_deal_card(self):
        card = Card('10')
        self.deck.deal_card.return_value = card
        dealt_card = self.dealer.deal_card()
        self.assertEqual(dealt_card, card)