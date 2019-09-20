from game_state import GameState
from player import Player

import inspect
import cards

class GameEngine:
    """The game engine of DominFUN, which runs the game.

    The GameEngine is instantiated by a FrontendController.

    The data flow out of the GameEngine is:
        the game turn, phase, and information is passed to the FrontendController

    The data flow into the GameEngine is:
        selected moves are passed into the GameEngine from the FrontendController
    
    The GameEngine manipulates the GameState based on moves provided by the FrontendController.

    The GameEngine does not run validation of moves, and passing in false information is undefined
    behavior. The frontend controller is in charge of validation and security, and should not pass
    any private objects to any unknown or unsafe Players"""

    def __init__(self):
        self.generate_available_cards()
        self.generate_starting_deck()

    def get_next_phase(self):
        pass

    def generate_available_cards(self):
        self.card_classnames = []
        self.card_classname_to_object = {}
        for name, obj in inspect.getmembers(cards):
            if name == "Card" or name == "CardType" or name == "Enum" or \
                name == "GameState" or name == "Phase" or name == "Player":
                continue
            if inspect.isclass(obj):
                self.card_classnames.append(name)
                self.card_classname_to_object[name] = obj
    
    def generate_starting_deck(self):
        copper = cards.Copper()
        estate = cards.Estate()
        self.default_starting_deck = ([copper] * 7) + ([estate] * 3)

    def initialize_gamestate(self, startingdeck=None, piles=None, num_players=2):
        if not startingdeck:
            self.default_starting_deck
        self.gamestate = GameState(startingdeck, piles, num_players)