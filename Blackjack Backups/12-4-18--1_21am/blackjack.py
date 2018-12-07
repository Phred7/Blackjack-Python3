import random
from blackjackPlayer import BlackjackPlayer

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

    def createHouse(self):
        self.house = BlackjackPlayer("House", False, True, 0);
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
            house = False;
            self.players.append(BlackjackPlayer(name, ai, house, balance));
            print("Player " + str(i+1) + ": " + str(name) + " has been created");
        ####must reset keeping players names and atributed but errasing hands -> method that erases hands in bjPlayer and in play() if loop>0 call reset() for loop that erases all hands including house
            
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
            print(str(self.players[i].getName()) + " has " + str(self.players[i].getPoints()) + "points availible");
        print("");
        print("--- --- --- --- ---");

    def calculate(self):
        houseTotal = self.house.getTotal();
        self.totals = [];
        print("");
        for i in range(self.numPlayers):
            self.totals.append(self.players[i].getTotal());
        for j in range(len(self.totals)):
            self.players[j].getHand();
            if(self.players[j].getBlackjack() == True): ##player gets a blackjack
                self.players[j].blackjack();
            elif(houseTotal == 21 and self.totals[j] == 21): ##house and player both get 21
                print("21==21");
                self.players[j].win();
            elif(self.house.getHouseBust() == True and self.players[j].getBust() == False): ##house busts player does not
                print("Hbust and Safe");
                self.players[j].win();
            elif(self.players[j].getBust() == True): ##player busts
                print("Bust");
                self.players[j].bust();
            elif(self.totals[j] < houseTotal and self.house.getHouseBust() == False): ##player total < house total and house doesnt bust
                print("total < Htotal <= 21");
                self.players[j].lost();
            elif(houseTotal <= self.totals[j] and self.totals[j] <= 21): ##player total <= house total and player total is <= 21
                print("Htotal < total <= 21");
                self.players[j].win();
            else:
                print("else")
                self.players[j].lost();               

    def rules(self):
        print("---Blackjack Rules---");

    def gameLogistice(self):
        print("Is there anything that needs to be changed?");

    def optionsLog(self):
        print("---Options---");

    def getGameStatus(self):
        return self.gameStatus;

    def gameOver(self):
        self.gameStatus = True;
        print("\n\n--- --- --- ---\n\n");
        print("Thanks for playing");
        print("\n\n--- --- --- ---\n\n");        

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
            else:
                print("Please enter a valid option");

    def resetHands(self):
        for i in range(self.numPlayers):
            self.players[i].eraseHand();
        ##self.house.eraseHand();
    
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

def main():
    game = Blackjack();
    
main();
