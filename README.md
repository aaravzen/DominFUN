# DominFUN
A Dominion Game Engine designed to battle bots (against other bots and real-life people).

The end goal is to have a Web Server implementation of the FrontendController that allows users to upload AI Bots (implementing the PlayerController).

# General Flow and Architecture
Flow starts in the FrontendController, which instantiates GameEngine and PlayerController objects. The GameEngine runs the game, using the GameState, Player, and Card classes to maintain state. The PlayerControllers are used to direct control of player actions to different pieces of code (whether a user-created and uploaded Dominion bot or a local human-controlled CLI).

The FrontendController receives the current player/phase of turn/current options from the GameEngine. It uses this information to direct control to the correct PlayerController in the correct paradigm. It waits on a selection made by the PlayerController. The PlayerController subclasses implement methods that take in available choices during a given phase and return an answer selection.

Once a selection has been made by the PlayerController and it has been communicated with the FrontendController, the FrontendController must validate choices and manage exception handling (due to the unknown nature of PlayerControllers, which may well be rando bots).

Then, the FrontendController alerts the GameEngine of the selection so that the GameEngine can update the game state and communicate the next player/phase/options to the FrontendController. The FrontendController will also give updates on a PlayerController's moves to all the other PlayerControllers.

# About
This project was created by Aarav Singh and John Gallagher (a DJAZ production). It started as a joke about a simple Big Money AI being able to beat a friend in a Dominion match. When we finish, we can find out for sure.

The game this is based on, [Dominion](https://en.wikipedia.org/wiki/Dominion_(card_game)), was made by Donald X. Vaccarino and published by Rio Grande Games. A big shoutout to them for making a game that has wasted hours and hours of our (and [others'](http://wiki.dominionstrategy.com/index.php/Main_Page)) time!

There's an [official online platform](https://dominion.games/) made and run by Shuffle iT and the physical base sets and expansions are available all over.

We were inspired by [Robot Game](https://github.com/RobotGame), an AI matchmaking game that put two teams of player-written bots in a head-to-head matchup. It ran on robotgame.org and was made by a dude named Brandon (as far as I know - I'm getting my history from an [unreliable source](https://old.reddit.com/r/robotgame) and this all happened quite a while ago). After Brandon stopped running it, [Peter Wen](https://github.com/WhiteHalmos) picked up the torch and hosted it on robotgame.net for a while. At the time of writing this, it's available to play [here](http://rg.robotgame.edu.pl/) - check it out!

We were also inspired by a (pretty darn difficult) [programming problem](https://pcs.cs.cloud.vt.edu/problems/231) written by Dr. Godmar Back at Virginia Tech.