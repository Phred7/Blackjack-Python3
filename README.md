# Blackjack-Python3

Uses Object Oriented Programming to allow the user/s to play blackjack against the house.
This includes 1-7 players, betting, doubling, splitting and the standard hitting and standing.
See printed rules (or the rules below) for other game specific details.

To play: Run the file named blackjackRunner and follow the IDLE/Terminal prompted statements

Please try to break this game and report any issues, bug or all help is appreciated!

Blackjack Rules:
Each palyer begins with a given number of points (or credits) that will be used to bet against the house.
The minimum bet per hand is 10 and the maximum bet is 100.
Bets are placed before you are dealt any cards and the House is dealt one card.
The goal of Blackjack is to get to as close to a current score of 21 as possible withour going over 21.
Each player is randomly dealt two cards.
Your current score (or points) is calculated by adding the face values of each card; 1 = 1pt, 10 = 10; J,Q,K = 10 (and appear as 10).
Aces are equal to 11 until you go above a total of 21 points but then equal 1.
A Blackjack is when your the first cards of your hand are an ace and a card with a value of 10.
On you turn you with have the options to (depending on you hand): hit, stand, split or double.
Hit: Hitting adds a random card to your hand and does not end your turn automatically.
Stand: Standing leaves you with the same hand and ends your turn.
Split: Spliting allows you to seperate your hand into two different hands both with one card but you are then dealt a new card for each hand. ...
On your turn you then will play both hands seperatly with the same options as a normal hand. ...
As a not splitting is only possible on you first hand with you first two cards which buts have the same value but do not need the same suit...
ie. card1 = 8 and card2 = 8, a split is possible; card1 = K and card2 = 10, a split is not possible.
Double: Doubling automaticaly doubles you bet and gives you one last card before ending your hand. ...
Doubling is only possible if your first two cards are less than 12 and only possible your first turn.
Once all players have had their turns the house plays:...
House rules: On the House's turn the house must hit until it's total is greater than 16.
When a player or the house goes over 21 that is known as a 'bust' or 'busting'...
players automatically lose if they bust even if the house busts.
A player loses if neither the house nor the player busts but the players total is less than the total of the house.
Lossing pays 1:1; ie: if player1 bets 25pts and loses, player1 loses 25pts from their total points (or credits).
A plater wins if the house busts and the player does not or if the palyer's total is greater than the house's total.
Winning pays 1:1; ie: if player1 bets 25pts and wins, player1 wins 25pts to their total points (or credits).
A Blackjack pays 3:2; ie: if player1 bess 20pts and gets a Blackjack, player1 wins 50pts to  their total points (or credits).
