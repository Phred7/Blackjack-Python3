import random
from blackjackPlayer import BlackjackPlayer
from blackjackHouse import BlackjackHouse

class Blackjack():
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
        self.numPlayers = 0;
        self.players = [];
        self.gameStatus = False;
        self.loop = 0;
        self.play();

    def getCard(self):
        index = random.randint(0, 12);
        card = self.cards[index]
        return card;

    def deal(self):
        for i in range(self.numPlayers):
            card1 = self.getCard();
            card2 = self.getCard();
            hand = [card1, card2];
            self.players[i].setHand(hand);
##            hand = [10, 10]
##            self.players[i].setHand(hand);

    def createHouse(self):
        self.house = BlackjackHouse();
        card1 = self.getCard();
        self.house.setHouse([card1]);

    def createPlayers(self):
        for i in range(self.numPlayers):
            print("");
            name = input("Name of player "+ str(i+1) + ": ");
            balance = int(input("How many points will " + str(name) + " start with?: "));
            if(balance < 10):
                balance = 10;
            ##ai = bool(input("Is " + str(name) + " a computer (True/False)?: "));
            ai = False;
            self.players.append(BlackjackPlayer(name, ai, balance));
            print("Player " + str(i+1) + ": " + str(name) + " has been created");
            
    def setPlayers(self):
        print("");
        self.numPlayers = int(input("How many players (min: 1, max: 7)?: "));
        while(self.numPlayers > 7 or self.numPlayers < 1):
            self.numPlayers = int(input("Error: Enter a valid number of players (min: 1, max: 7): "));

    def getHands(self):
        self.house.getHouse();
        for i in range(self.numPlayers):
            self.players[i].getHand();
        print("");
        print("--- --- --- --- ---");
               
    def turn(self):
        for i in range(self.numPlayers):
            self.players[i].options();
            print("");
            print("");
        self.house.houseHits();
        print("");
        print("");

    def placeBets(self):
        for i in range(self.numPlayers):
            self.players[i].placeBet();
        print("");
        print("--- --- --- --- ---");

    def getTotals(self):
        for i in range(self.numPlayers):
            self.players[i].updateTotal();
            print(str(self.players[i].getName()) + " has " + str(self.players[i].getTotal()) + "points availible");
        print("");
        print("--- --- --- --- ---");

    def getPoints(self):
        for i in range(self.numPlayers):
            if(self.players[i].getPoints() == 0):
                print(str(self.players[i].getName()) + " has been removed because " + str(self.players[i].getName()) + " has " + str(self.players[i].getPoints()) + "points availible");
                self.players = self.players.pop(i)
                i += -1
                self.numPlayers += -1
            else:
                print(str(self.players[i].getName()) + " has " + str(self.players[i].getPoints()) + "points availible");
        print("");
        print("--- --- --- --- ---");

    def rules(self):
        self.printLineReturns(8);
        print("---Blackjack Rules---");
        print("Each palyer begins with a given number of points (or credits) that will be used to bet against the house.")
        print("The minimum bet per hand is 10 and the maximum bet is 100.")
        print("Bets are placed before you are dealt any cards and the House is dealt one card.\n")
        print("The goal of Blackjack is to get to as close to a current score of 21 as possible withour going over 21.\n");
        print("Each player is randomly dealt two cards.\n");
        print("Your current score (or points) is calculated by adding the face values of each card; 1 = 1pt, 10 = 10; J,Q,K = 10 (and appear as 10).");
        print("Aces are equal to 11 until you go above a total of 21 points but then equal 1.");
        print("A Blackjack is when your the first cards of your hand are an ace and a card with a value of 10.\n");
        print("On you turn you with have the options to (depending on you hand): hit, stand, split or double.");
        print("Hit: Hitting adds a random card to your hand and does not end your turn automatically.\n");
        print("Stand: Standing leaves you with the same hand and ends your turn.\n");
        print("Split: Spliting allows you to seperate your hand into two different hands both with one card but you are then dealt a new card for each hand. ...");
        print("On your turn you then will play both hands seperatly with the same options as a normal hand. ...");
        print("As a not splitting is only possible on you first hand with you first two cards which buts have the same value but do not need the same suit...");
        print("ie. card1 = 8 and card2 = 8, a split is possible; card1 = K and card2 = 10, a split is not possible.\n");
        print("Double: Doubling automaticaly doubles you bet and gives you one last card before ending your hand. ...");
        print("Doubling is only possible if your first two cards are less than 12 and only possible your first turn.\n");
        print("Once all players have had their turns the house plays:...");
        print("House rules: On the House's turn the house must hit until it's total is greater than 16.\n");
        print("When a player or the house goes over 21 that is known as a 'bust' or 'busting'...");
        print("players automatically lose if they bust even if the house busts.\n");
        print("A player loses if neither the house nor the player busts but the players total is less than the total of the house.");
        print("Lossing pays 1:1; ie: if player1 bets 25pts and loses, player1 loses 25pts from their total points (or credits).");
        print("A plater wins if the house busts and the player does not or if the palyer's total is greater than the house's total.");
        print("Winning pays 1:1; ie: if player1 bets 25pts and wins, player1 wins 25pts to their total points (or credits).");
        print("A Blackjack pays 3:2; ie: if player1 bess 20pts and gets a Blackjack, player1 wins 50pts to  their total points (or credits).");
        print("---Blackjack Rules---");
        self.printLineReturns(1);

    def gameLogistice(self):
        print("Is there anything that needs to be changed?");

    def optionsLog(self):
        print("---Options---");

    def getGameStatus(self):
        return self.gameStatus;

    def printLineReturns(self, num):
        num = int(num/2)
        for i in range(num):
            print("\n");

    def gameOver(self):
        self.gameStatus = True;
        self.printLineReturns(16);
        print("--- --- --- --- ---\n\n");
        print("Thanks for playing!");
        print("\n\n--- --- --- --- ---");
        self.printLineReturns(16);

    def gameContinue(self):
        self.gameStatus = False;
        print("\n\n--- --- --- ---\n");
        self.getPoints();

    def isGameOver(self):
        print("\n\n--- --- --- ---\n\n");
        print("Play Again?");
        choice = 0;
        while(choice == 0):
            gameStatus = input("Yes or No: ").lower();
            if(gameStatus == "yes"):
                self.gameContinue();
                choice = 1;
            elif(gameStatus == "no"):
                self.gameOver();
                choice = 1;
            elif(gameStatus == "nope"):
                while(True):
                    print("Wardling")
            else:
                print("Please enter a valid option");

    def resetHands(self):
        for i in range(self.numPlayers):
            self.players[i].eraseHand();
    
    def play(self):
        self.rules();
        self.setPlayers();
        self.createPlayers();
        while(self.gameStatus == False):
            if(self.loop > 0):
                self.resetHands();
            self.createHouse();
            self.placeBets();
            self.deal();
            self.getHands();
            self.turn();
            self.calculate();
            self.isGameOver();
            self.loop += 1;

    def calculate(self):
        print("Calculating...")
        for i in range(self.numPlayers):
            if(self.players[i].getSplit() == True):
                self.players[i].points = self.players[i].calculateSplit(self.house.getHouseBust(), self.house.getTotal());
            elif(self.players[i].getBlackjack() == True):
                self.players[i]._blackjack();
            elif(self.players[i].getBust() == True):
                self.players[i].bust();
            elif(self.house.getHouseBust() == True):
                if(self.players[i].getBust() == False):
                    self.players[i].win();
                else:
                    self.players[i].lost();
            elif(self.house.getHouseBust() == False):
                if(self.players[i].getTotal() >= self.house.getTotal()):
                    self.players[i].win();
                else:
                    self.players[i].lost();
            else:
                print("else - final");

def main():
    game = Blackjack();
    
main();
