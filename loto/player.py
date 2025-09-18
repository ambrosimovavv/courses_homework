from card import Card
class Player:

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.card = None

    def get_card(self):
        self.card = Card()
