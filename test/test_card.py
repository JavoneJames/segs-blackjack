import unittest
from src.card import Card


class CardTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.card = Card()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_get_card_value(self):
        # Test for a card with rank '10'
        card = Card('10')
        result = card.get_value()
        self.assertEqual(result, 10)  # Checking if it returns 10 for '10'
        
        # Test for a face card 'J'
        card = Card('J')
        result = card.get_value()
        self.assertEqual(result, 10)  # Checking if it returns 10 for 'J'

        # # Test for Ace card - this should fail is uncommented
        # card = Card('2')
        # result = card.get_value()
        # self.assertEqual(result, 11)  # Checking if it returns 11 for 'A'




if __name__ == '__main__':
    unittest.main()
