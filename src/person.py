class Person:

    def __init__(self):
        self.cards = []

    # add a card to the person's hand
    def retrieve_card(self, card):
        self.cards.append(card)