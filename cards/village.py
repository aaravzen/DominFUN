from card import *

class Village(Card):
    name = "Village"
    cardtypes = [CardType.ACTION, CardType.BUYABLE]

    def __init__(self):
        pass

    def do_thing(self, cardtype, gamestate, player):
        if cardtype == CardType.ACTION:
            player.actions += 2
            player.draw_cards(1)
        super().do_thing(cardtype, gamestate, player)