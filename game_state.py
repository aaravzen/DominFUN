from enum import Enum
from player import Player

class GameState:
    """The GameState class keeps track of all the cards, decks, and doohickies involved.

    Mostly just a data store, but holds methods like add_player to manipulate the game state.

    No validation because only a dummy would pass this to PlayerControllers
    
    (please remember not to pass to PlayerControllers)
    
    Passed into cards to alter game state attributes"""

    def __init__(self, startingdeck, piles, num_players):
        self.startingdeck = startingdeck
        self.piles = piles
        self.players = []
        self.add_players(num_players)
        self.next_player = 0
    
    def add_players(self, num_players):
        for _ in range(num_players):
            self.players.append(Player(deck=self.startingdeck.copy()))
    
    def get_next_player(self):
        ret = self.players[self.next_player]
        self.next_player += 1
        self.next_player %= len(self.players)
        return ret
    
class Phase(Enum):
    ACTION = 1
    SPENDING = 2
    BUYING = 3