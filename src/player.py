from src.person import Person

class Player(Person):

    def __init__(self, dealer, avaiable_balance = 1000):
        super().__init__()
        self.dealer = dealer
        self.avaiable_balance = avaiable_balance
        self.wager = 0