from game_state import GameState
from player import Player

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

    def __init__(self, startingdeck, piles, num_players=2):
        self.gamestate = GameState(startingdeck, piles, num_players)

    def get_next_phase(self):
        