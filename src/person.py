class Person:

    def __init__(self):
        self.cards = []

    # add a card to the person's hand
    def retrieve_card(self, card):
        self.cards.append(card)
    
    # calc score for the current hand held by a perosn
    def score(self):
        total = 0
        ace_count = 0
        # loop through cards held by a person and add face value to total
        for card in self.cards:
            card_value = card.get_value()
            total += card_value
            if card.rank == 'A': # if card is an ace incerement counter
                ace_count += 1
        # loop is valid is total over 21 and ace counter greater than 0
        while total > 21 and ace_count:
            total -= 10  # convert Ace from 11 to 1
            ace_count -= 1

        return total