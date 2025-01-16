from src.person import Person

class Dealer(Person):

    def __init__(self, deck):
        super().__init__()
        self.deck = deck