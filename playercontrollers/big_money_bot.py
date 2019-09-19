from player_controller import PlayerController

class BigMoneyBot(PlayerController):
    """This is a simple bot that buys provinces/golds/silvers in that order when it can.
    
    Actions are for the weak and nimble-minded. The face hunter of Dominion.
    
    gg ez no re"""

    # def pick_action(self, action_cards) commenting this out because WE DON'T NEED ACTIONS baby
    
    def pick_treasure(self, treasure_cards):
        # literally just spend all the money we can bro don't even worry about it
        return treasure_cards[0]
    
    def buy_card(self, buyable_cards):
        # you see, it's a simple 3-step process
        for card in buyable_cards:
            if card.name == "Province":
                return card
        for card in buyable_cards:
            if card.name == "Gold":
                return card
        for card in buyable_cards:
            if card.name == "Silver":
                return card
        