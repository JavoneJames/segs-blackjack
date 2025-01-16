from src.person import Person

class Dealer(Person):

    def __init__(self, deck):
        super().__init__()
        self.deck = deck

    # calls shuffle_deck method from Deck to shuffle cards
    def shuffle_deck(self):
        self.deck.shuffle_deck()