from src.deck import Deck
from src.dealer import Dealer
from src.player import Player

class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.player = Player(self.dealer)

if __name__ == '__main__':
    play()
