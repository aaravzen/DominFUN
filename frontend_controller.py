import sys
sys.path.append("playercontrollers")

from game_engine import GameEngine

class FrontendController:
    """This is where the magic happens.

    Here, we'll instantiate a GameEngine and PlayerControllers.

    The GameEngine will run the game based on specifications (starting decks, piles) from here.

    The next phase of play, along with the GameState, will be passed here by the GameEngine.

    The FrontendController is responsible for delivering a player or AI choice of action back to
    the GameEngine to be executed. The FrontendController should not deliver the GameState object
    to any PlayerControllers because they may be devious AI hacker bots :4o

    We'll make this big boy do web server things (ie. communicate options to human players or possibly
    uploaded custom AI PlayerControllers online). For now it's just gonna be a good ol' CLI"""

    # TODO: Make sure any PlayerControllers instantiated are actual subclasses of PlayerController

    def __init__(self):
        self.game_engine = GameEngine()

if __name__ == '__main__':
    FE = FrontendController()