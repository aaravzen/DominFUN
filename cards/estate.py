from card import *

class Estate(Card):
    name = "Estate"
    cardtypes = [CardType.VICTORY_POINT, CardType.BUYABLE]

    def __init__(self):
        pass

    def do_thing(self, phase, gamestate, player):
        if phase == Phase.BUYING:
            player.victory_points += 1
        super().do_thing(phase, gamestate, player)