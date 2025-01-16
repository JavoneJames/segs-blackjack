from src.card import Card
from random import shuffle


class Deck:

    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank) for rank in self.ranks for _ in range(4)]

    # Shuffle deck of cards
    def shuffle_deck(self):
        print("Dealer shuffling cards...")
        shuffle(self.cards)

    # deal a single card from the deck
    def deal_card(self):
        return self.cards.pop()