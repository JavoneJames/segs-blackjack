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

    def collect_wagers(self):
        user_input = 0
        print(f"Your available balance is: {self.player.balance()}")
        while True:
            user_input = int(input("How much would you like to wager? "))
            if user_input > 0 and user_input <= self.player.balance():
                self.player.set_wager(user_input)
                break
            elif user_input <= 0:
                print("Invalid input, please try again. Input should be a whole number")
            else:
                print("Insufficient balance, wager amoutn too high!")

    def show_initial_cards(self):
        # display player's cards and score
        print(f"Player's card: {self.player}")
        print("Player's score:", self.player.score())
        # display dealer's first card (only the upcard)
        print("Dealer's upcard:", self.dealer.cards[0].rank)

    def play(self):
        # add game logic for player and dealer turns
        self.player.turn()
        if self.player.score() <= 21:
            self.dealer.turn()
        else:
            print("Player busts! Dealer wins!")
        
        self.determine_outcome()

if __name__ == '__main__':
    bj = BlackJack()
    bj.set_up_game()
    bj.play()

