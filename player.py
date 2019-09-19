class Player:
    """Used to store player-specific attributes such as hand, deck, discard

    Also used to track turn-based elements such as 
    
    Passed into cards to alter player attributes"""

    def __init__(self, deck=[], hand=[], discard=[]):
        self.deck = deck
        self.hand = []
        self.discard = []
        self.turn_number = 0
        self.victory_points = self.calculate_victory_points()

        self.reset_turn()

    def discard_hand(self):
        pass

    def draw_cards(self, num_cards=5):
        pass

    def reset_turn(self):
        self.discard_hand()
        self.draw_cards()
        self.actions = 1
        self.buying_power = 0
        self.turn_number += 1

    def holding_card_of_type(self, cardtype):
        return any(card.is_type(cardtype) for card in self.hand)
    
    def add_to_discard(self, card):
        self.discard.append(card)
    
    def calculate_victory_points():
        pass
