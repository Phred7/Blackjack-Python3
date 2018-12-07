import random
from blackjackSplit import BlackjackSplit as Split

class BlackjackPlayer():
    def __init__(self, name, aiBool, houseBool, startingBalance):
        self.minBet = 10; ##usually 10 or 15
        self.maxBet = 100;
        self.computer = aiBool; ##True or False
        self.house = houseBool; ##True or False
        self.name = name; ##string name of player
        self.total = 0;
        self.points = startingBalance; ##starting number of points to be betted with
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
        self.isTurnOver = False;
        self.houseBust = False;
        self.blackjack = False;
        self.bust = False;

    def delete(self):
        pass;

    def editName(self):
        pass;

    def getName(self):
        return self.name;

    def eraseHand(self):
        self.hand = [];
        self.total = 0;
        self.isTurnOver = False;
        self.houseBust = False;
        self.blackjack = False;
        self.bust = False;

    def getPoints(self):
        return self.points;
    
    def updateTotal(self):
        self.total = 0;
        for i in range(len(self.hand)):
                self.total += self.hand[i];

    def getTotal(self):
        return self.total;
        
    def getHand(self):
        print("");
        print("---" + str(self.name) + "'s hand---");
        for i in range(len(self.hand)):
                print(str(self.hand[i]));
        if(self.blackjack == True):
            print("Total: " + str(self.total) + " = BLACKJACK");
        else:
            print("Total: " + str(self.total));
        print("Bet: " + str(self.bet) + "points");
        
    def setHand(self, hand):
        self.hand = hand;
        for i in range(len(self.hand)):
            self.total += self.hand[i];
        self.checkBlackjack();

    def checkBlackjack(self):
        if((self.hand[0] == 11 and self.hand[1] == 10) or (self.hand[0] == 10 and self.hand[1] == 11)):
            self.blackjack = True;
        else:
            self.blackjack = False;
    
    def hit(self):
        index = random.randint(0, 12);
        card = self.cards[index]
        self.hand.append(card);
        print(str(self.name) + " recieved a: " + str(card));
        self.isTurnOver = False;

    def stand(self):
        print(str(self.name) + " decided to Stand");
        self.isTurnOver = True;

    def double(self):
        print(str(self.name) + " decided to Double");
        self.bet = 2 * self.bet
        self.hit();
        self.isTurnOver = True;

    def split(self):
        print(str(self.name) + " decided to Split");
        Split(self.hand, self.bet, self.points)
        self.isTurnOver = True;

    def placeBet(self):
        print("");
        self.bet = int(input(str(self.name) + "'s avalible points: " + str(self.points) + "\nHow many points will " + str(self.name) + " bet?: "));
        while(self.points < self.bet or self.bet < self.minBet or self.maxBet < self.bet):
            self.bet = int(input("Invalid bet. Avalible points: " + str(self.points) + ". How many will you bet?: "))
        print("Bet: " + str(self.bet) + "points");

    def options(self):
        while(self.isTurnOver == False):
            self.updateTotal();
            print("");
            print("---" + str(self.name) + "'s turn---");
            print("Hand" + str(self.hand));
            print("Total " +str(self.total));
            if(self.blackjack == True):
                print(str(self.name)+" got a blackjack");
                self.isTurnOver = True;
                print("Your turn is over");
            elif(self.total < 21):
                choice = 0;
                while(choice == 0):
                    print("Options:");
                    print("1. Hit");
                    print("2. Stand");
##                    if(self.hand[0] == self.hand[1]): ##split is possible
##                        print("3. Split");
                    if(self.total <= 11): ##double is possible
                        print("4. Double");
                    choice = int(input("Your choice: "));
                    if(choice == 1):
                        self.hit();
                    elif(choice == 2):
                        self.stand();
##                    elif(self.hand[0] == self.hand[1] and choice == 3):
##                        self.split();
                    elif(self.total <= 11 and choice == 4):
                        self.double();
                    else:
                        choice = 0;
                        print("That option is invalid. Try again:");
            elif(self.total == 21 and self.blackjack == False):
                print("Your total is: " + str(self.total));
                self.isTurnOver = True;
            else:
                self.isTurnOver = True;
        self.updateTotal();
        self.getHand();
        if(self.total == 21 and self.blackjack == False):
            print("Your total is: " + str(self.total));
            print("Your turn is over");
        elif(self.total > 21):
            print(str(self.name) + " bust");
            print("Your turn is over");
            self.bust = True;
        else:
            self.bust = False;
            print("Your turn is over");
            
    def isComputer(self):
        if(self.computer == True):
            return True;
        else:
            return False;
        
    def getProbability(self, total): ##used for the computer to calculate whether or not to hit
        pass;

    def isHouse(self):
        if(self.house == True):
            return True;
        else:
            return False;

    def setHouse(self, hand):
        self.hand = hand;

    def getHouse(self):
        if(self.house == True):
            print("");
            print("---" + str(self.name) + "'s hand---");
            for i in range(len(self.hand)):
                print(str(self.hand[i]));
            self.updateTotal();
            print("Total: " + str(self.total));

    def getAces(self):
        self.aces = 0;
        for i in range(len(self.hand)):
            if(self.hand[i] == 11):
                self.aces += 1;
        return self.aces;

    def houseHits(self):
        print("");
        print("---House's turn---");
        if(self.house == True):
            while(self.total <= 16):
                self.aces = 0;
                self.updateTotal();
                if(self.total <= 16):
                    self.hit();
                self.getAces();
                if(self.total > 21 and self.aces > 0):
                    self.total = self.total - (self.aces * 10);
                elif(self.total > 21):
                    self.houseBust = True
            if(self.houseBust == True):
                print("The House Busts");
                self.getHouse();
            elif(self.blackjack == True):
                print("The House got a BLACKJACK");
                self.getHouse();
            else:
                self.getHouse();
        print("")
        print("--- --- --- --- ---");

    def getBust(self):
        return self.bust;

    def getHouseBust(self):
        return self.houseBust;

    def getBlackjack(self):
        return self.blackjack;
    
    def win(self):
        self.points += self.bet;
        print(str(self.name) + " won " + str(self.bet) + "points. Total: " + str(self.points) + "points.");

    def lost(self):
        self.points = self.points - self.bet;
        print(str(self.name) + " lost. Remaining points: " + str(self.points));
        
    def bust(self):
        self.points = self.points - self.bet;
        print(str(self.name) + " bust. Remaining points: " + str(self.points));

    def blackjack(self):
        self.blkjackIncrease = self.bet + int(((3/2)(self.bet)))
        self.points += (self.bet + int(((3/2)(self.bet))));
        print(str(self.name) + " got a blackjack and won " + str(self.blkjackIncrease) + "points. Total: " + str(self.points) + "points.");
