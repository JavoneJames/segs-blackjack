class Card:

    def __init__(self, rank):
        self.rank = rank

    # return the value of a card
    def get_value(self):
        face_cards = ('J', 'Q', 'K')
        if self.rank in face_cards:
            return 10
        elif self.rank  == 'A':
            return 11
        else:
            return int(self.rank)
        
    # return card rank as a string
    def __str__(self):
        return self.rank