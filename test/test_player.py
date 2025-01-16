import unittest
from src.player import Player

class PlayerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.player = Player()

    def tearDown(self):  # this method will be run after each test
        pass

    """ Given I have a valid hand of cards
        When I choose to ‘hit’
        Then I receive another card
        And my score is updated """
    @patch('builtins.input', side_effect=['h', 's'])
    def test_player_hit(self, mock_choose_action):
        initial_score = self.player.score()
        self.player.turn()
        self.assertGreater(len(self.player.cards), 2, "Player should have more than 2 cards after hitting")
        self.assertGreater(self.player.score(), initial_score, "Player's score should be updated after hitting")