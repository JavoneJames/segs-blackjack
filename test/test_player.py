import unittest
from src.player import Player

class PlayerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.person = Player()

    def tearDown(self):  # this method will be run after each test
        pass

    