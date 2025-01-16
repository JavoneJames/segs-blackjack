from src.person import Person

class Player(Person):

    def __init__(self, dealer, available_balance = 1000):
        super().__init__()
        self.dealer = dealer
        self.available_balance = available_balance
        self.wager = 0

    # return the player's available balance
    def balance(self):
        return self.available_balance
    
    # allow the player to set the wager amount
    def set_wager(self, wager_amount):
        self.wager = wager_amount

    # update player balance after winning or lossing a game
    def update_balance(self, win):
        if win:
            self.available_balance += (self.wager * 2)
        else:
            self.available_balance -= self.wager
        self.wager = 0
    # ask the player whether or not they want to hit or stand
    def choose_action(self):
        user_input = input("Would you like to [H]it or [S]tand? ").lower()
        return user_input
    
    def turn(self):
        while True:
            user_input = self.choose_action()
            if user_input == 'h':
                temp = self.dealer.deal_card()
                self.retrieve_card(temp)
                print("Player decides to HIT!")
                print(f"Card drawn by Player is {temp}")
                print(f"Player's cards {self}")
                print("Player's score:", self.score())

                if self.score() > 21:
                    print("You bust! Game over.")
                    break
            elif user_input == 's':
                print("Player decides to STAND!")
                print(f"Player's cards {self}")
                print("Player's score:", self.score())
                break
            else:
                print("Invalid choice. Pleases choose [H]it or [S]tand")
    
    def __str__(self):
        hand = [str(card) for card in self.cards]
        return f"{hand}"