from card import *

class Copper(Card):
    name = "Copper"
    cardtypes = [CardType.TREASURE, CardType.BUYABLE]

    def __init__(self):
        pass

    def do_thing(self, phase, gamestate, player):
        if phase == Phase.SPENDING:
            player.buying_power += 1
        super().do_thing(phase, gamestate, player)