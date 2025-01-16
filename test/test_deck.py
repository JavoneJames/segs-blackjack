import unittest
from src.deck import Deck


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_number_of_cards(self):  # any method beginning with 'test_' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)
    
    # Test if shuffling the deck changes the order
    def test_shuffle_deck(self):
        original_order = self.deck.cards[:]
        self.deck.shuffle_deck()
        shuffled_order = self.deck.cards
        self.assertNotEqual(original_order, shuffled_order)

    # Test if dealing a card removes it from the deck
    def test_deal_card(self):
        original_deck_size = len(self.deck.cards)
        self.assertEqual(len(self.deck.cards), original_deck_size - 1)



if __name__ == '__main__':
    unittest.main()
