# DominFUN
A Dominion Game Engine designed to battle bots (against other bots and real-life people).

The end goal is to have a Web Server implementation of the FrontendController that allows users to upload AI Bots (implementing the PlayerController).

# General Flow and Architecture
Flow starts in the FrontendController, which instantiates GameEngine and PlayerController objects. The GameEngine runs the game, using the GameState, Player, and Card classes to maintain state. The PlayerControllers are used to direct control of player actions to different pieces of code (whether a user-created and uploaded Dominion bot or a local human-controlled CLI).

The FrontendController receives the current player/phase of turn/current options from the GameEngine. It uses this information to direct control to the correct PlayerController in the correct paradigm. It waits on a selection made by the PlayerController. The PlayerController subclasses implement methods that take in available choices during a given phase and return an answer selection.

Once a selection has been made by the PlayerController and it has been communicated with the FrontendController, the FrontendController must validate choices and manage exception handling (due to the unknown nature of PlayerControllers, which may well be rando bots).

Then, the FrontendController alerts the GameEngine of the selection so that the GameEngine can update the game state and communicate the next player/phase/options to the FrontendController. The FrontendController will also give updates on a PlayerController's moves to all the other PlayerControllers.
