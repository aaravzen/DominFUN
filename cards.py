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
        self.actions_given_by_action = 0
        self.cards_given_by_action = 0
        self.buys_given_by_action = 0

        self.buying_power_when_spent = 0

        self.victory_points_when_bought = 0
        
        self.cost = 0

    def is_type(self, cardtype):
        return cardtype in self.cardtypes

    def do_thing(self, phase, gamestate, player):
        print("doing thing")
        # cards don't have to implement generic things - it can just call super() after supplying facts in init
        if phase == Phase.ACTION:
            player.actions += 2
            player.draw_cards(1)
        if phase == Phase.SPENDING:
            player.buying_power += self.buying_power_when_spent
        if phase == Phase.BUYING:
            player.victory_points += self.victory_points_when_bought
            player.add_to_discard(self)
            # TODO add it to the player's discard. Not sure if the following actually does what I want it to.
            # Also we if there's only one of each card object, we need to not pass them to the PlayerControllers.
    
    def __repr__(self):
        return self.name

class CardType(Enum):
    ACTION = 1
    TREASURE = 2
    VICTORY_POINT = 3
    BUYABLE = 4 # for determining if it can be bought, not if it's being bought


########## Cards go under here. The were in their own dir but... that's too many files and too many imports
########## Do we want to read them from a data file instead of making them subclasses? Maybe.
########## Is it too early for tech debt? Never!

########## Basic Cards
##### Treasure
class Copper(Card):
    name = "Copper"
    cardtypes = [CardType.TREASURE, CardType.BUYABLE]

    def __init__(self):
        super().__init__()
        self.buying_power_when_spent = 1

class Silver(Card):
    name = "Silver"
    cardtypes = [CardType.TREASURE, CardType.BUYABLE]

    def __init__(self):
        super().__init__()
        self.buying_power_when_spent = 2
        self.cost = 3

class Gold(Card):
    name = "Gold"
    cardtypes = [CardType.TREASURE, CardType.BUYABLE]

    def __init__(self):
        super().__init__()
        self.buying_power_when_spent = 3
        self.cost = 6

##### Victory
class Estate(Card):
    name = "Estate"
    cardtypes = [CardType.VICTORY_POINT, CardType.BUYABLE]

    def __init__(self):
        super().__init__()
        self.victory_points_when_bought = 1
        self.cost = 2

class Duchy(Card):
    name = "Duchy"
    cardtypes = [CardType.VICTORY_POINT, CardType.BUYABLE]

    def __init__(self):
        super().__init__()
        self.victory_points_when_bought = 3
        self.cost = 5

class Province(Card):
    name = "Province"
    cardtypes = [CardType.VICTORY_POINT, CardType.BUYABLE]

    def __init__(self):
        super().__init__()
        self.victory_points_when_bought = 6
        self.cost = 8

########## Base Set Kingdom Cards
##### Action
class Village(Card):
    name = "Village"
    cardtypes = [CardType.ACTION, CardType.BUYABLE]

    def __init__(self):
        super().__init__()
        self.actions_given_by_action = 2
        self.cards_given_by_action = 1
        self.cost = 3

##### Action-Attack

##### Action-Reaction

##### Victory