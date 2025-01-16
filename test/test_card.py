import unittest
from src.card import Card


class CardTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.card = None

    def tearDown(self):  # this method will be run after each test
        pass

    # Test for number card '10'
    def test_get_card_value_number(self):
        self.card = Card('10')
        result = self.card.get_value()
        self.assertEqual(result, 10)

    # Test for a face card like 'J'
    def test_get_card_value_face_card(self):
        self.card = Card('J')
        result = self.card.get_value()
        self.assertEqual(result, 10)

    # def test_get_card_low_value_number(self):
    # # Test for 2 card - this should fail is uncommented
    #     card = Card('2')
    #     result = card.get_value()
    #     self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()
