from src.person import Person

class Dealer(Person):

    def __init__(self, deck):
        super().__init__()
        self.deck = deck

    # calls shuffle_deck method from Deck to shuffle cards
    def shuffle_deck(self):
        self.deck.shuffle_deck()

    # call deal_card method from Deck to deal a card
    def deal_card(self):
        return self.deck.deal_card()

    # reveal the dealer's cards (all cards)
    def reveal_cards(self):
        hand = [str(card) for card in self.cards]
        print("Dealer's cards:", hand)