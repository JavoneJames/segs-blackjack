import unittest
from src.person import Person

class PersonTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.person = Person()

    def tearDown(self):  # this method will be run after each test
        pass
    
    # test that a person with no cards has a score of 0
    def test_empty_hand(self):
        self.assertEqual(self.person.score(), 0)

    # test that a person with 2 cards has the correct score
    def test_two_cards(self):
        pass
    
    # test that the score is calculated for multiple cards
    def test_multiple_cards(self):
        pass