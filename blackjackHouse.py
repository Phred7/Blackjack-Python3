import random

class BlackjackHouse():
    def __init__(self):
        self.name = "House"; ##string name of player
        self.total = 0;
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
        self.house = True;
        self.isTurnOver = False;
        self.houseBust = False;
        self.blackjack = False;

    def getName(self):
        return self.name;

    def eraseHand(self):
        self.hand = [];
        self.total = 0;
        self.isTurnOver = False;
        self.houseBust = False;
        self.blackjack = False;
        self.bust = False;
    
    def updateTotal(self):
        #print("Total: " + str(self.total));
        self.total = 0;
        length = len(self.hand);
        for i in range(length):
            self.total += self.hand[i];

    def getTotal(self):
        return self.total;
        
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
        ##print(self.aces)

    def houseHits(self):
        print("");
        print("---House's turn---");
        if(self.house == True):
            looper = True;
            while(looper == True):
                self.updateTotal();
                self.getAces();
                if(self.total <= 16):
                    self.hit();
                if(self.total > 21 and self.aces > 0):
                    self.total = self.total - (self.aces * 10);
                    for i in range(len(self.hand)):
                        if(self.hand[i] == 11):
                            self.hand[i] = 1;
                elif(self.total > 21):
                    self.houseBust = True
                    looper = False;
                elif(self.total <= 21 and self.total > 16):
                    looper = False;
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


    def getHouseBust(self):
        return self.houseBust;

    def getBlackjack(self):
        return self.blackjack;
