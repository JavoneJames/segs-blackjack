from src.deck import Deck
from src.dealer import Dealer
from src.player import Player

class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.player = Player(self.dealer)

    def set_up_game(self):
        self.collect_wagers()
        self.dealer.shuffle_deck()
        # deal two cards to the player and two cards to the dealer
        self.player.retrieve_card(self.dealer.deal_card())  # player gets card
        self.dealer.retrieve_card(self.dealer.deal_card())  # dealer gets card (1st card)
        self.player.retrieve_card(self.dealer.deal_card())  # player gets card
        self.dealer.retrieve_card(self.dealer.deal_card())  # dealer gets card (2nd card)
        # show the initial cards and scores
        self.show_initial_cards()

if __name__ == '__main__':
    bj = BlackJack()
    bj.set_up_game()
    bj.play()

