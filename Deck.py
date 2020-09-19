def Deck:
    def __init__(self):
        self.cards = dict()

    def add_card(self, card):
        self.cards[card] = 

    def remove_card(self, card):
        self.cards.remove(card)

    def export_to_csv(self, filename):
        with open(filename + ".csv", "w") as f:
            pass
