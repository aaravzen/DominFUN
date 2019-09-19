from enum import Enum
from player import Player
from game_state import GameState, Phase

class Card:
    """So this one represents a card. Holds the actions and values.
    
    Should be the parent class of all cards, which should override the (relevant) fields/methods here.
    
    Unless they don't want do anything, in which case they don't have to :)"""
    name = "Card Name"
    cardtypes = []

    def __init__(self):
        pass

    def is_type(self, cardtype):
        return cardtype in self.cardtypes

    def do_thing(self, phase, gamestate, player):
        # cards don't have to implement generic buying - it can just call super()
        if phase == Phase.BUYING:
            # TODO add it to the player's discard. Not sure if the following actually does what I want it to.
            # Also we if there's only one of each card object, we need to not pass them to the PlayerControllers.
            player.add_to_discard(self)

class CardType(Enum):
    ACTION = 1
    TREASURE = 2
    VICTORY_POINT = 3
    BUYABLE = 4 # for determining if it can be bought, not if it's being bought