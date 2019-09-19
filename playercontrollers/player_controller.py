class PlayerController:
    """This is what you gotta implement if you make a player controller.

    Instantiation is up to the FrontendController, so that'll have to communicate with
    the user to figure out who/what/when/where the intended PlayerControllers are.

    The PlayerController will be given possible cards to play at any phase of their turn.

    The PlayerController will also be delivered with updates on what opponents do (probably,
    assuming the FrontendController isn't slacking on the job).

    By implementing these methods, the AI or human interface can communicate back with the
    FrontendController, which will then:
        validate the moves,
        let the GameEngine take care of resolving any actions or effects of the card, and
        pass options to the next PlayerController/pass updates to other PlayerControllers.
    
    Technically this isn't an abstract class at the moment. so any subclasses that don't
    implement these will just do nothing. and if a PlayerController isn't a subclass or this
    things will probably break. Should probably make sure the """
    
    def pick_action(self, action_cards):
        """passes in a list of playable action cards (in the player's hand).

        expects a return of one of those references or None, if the player doesn't want to play one"""
        return None
    
    def pick_treasure(self, treasure_cards):
        """passes in a list of playable treasure cards (in the player's hand).

        expects a return of one of those references or None, if the player is done spending money"""
        return None
    
    def buy_card(self, buyable_cards):
        """passes in a list of playable treasure cards (in the player's hand).

        expects a return of one of those references or None, if the player is done spending money"""
        return None