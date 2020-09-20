def Deck:
    def __init__(self):
        self.cards = None

    def add_card(self, card):
        raise NotImplementedError

    def remove_card(self, card):
        raise NotImplementedError

    def export_to_csv(self, filename):
        with open(filename + ".csv", "w") as f:
            pass

    def export_to_anki(self, filename):
        raise NotImplementedError
