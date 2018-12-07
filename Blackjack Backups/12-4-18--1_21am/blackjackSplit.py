import random

class BlackjackSplit():
    def __init__(self, hand, bet, balance):
        self.bet = self.bet2 = bet;
        self.hand = self.hand2 = hand[0];
        self.total = self.total2 = 0;
        self.points = balance;
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
        self.getHand;
        self.getHand2;
        
    def getHand(self):
        print("");
        print("---" + str(self.name) + "'s first hand---");
        for i in range(len(self.hand)):
                print(str(self.hand[i]));
        print("Total: " + str(self.total));
        if(self.blackjack == True):
            print("BLACKJACK");              

    def checkBlackjack(self):
        if((self.hand[0] == 11 and self.hand[1] == 10) or (self.hand[0] == 10 and self.hand[1] == 11)):
            self.blackjack = True;
        else:
            self.blackjack = False;
    
    def hit(self):
        index = random.randint(0, 12);
        card = self.cards[index]
        self.hand.append(card);
        print(str(self.name)+" recieved a: " + str(card) + "in hand 1");

    def stand(self):
        print(str(self.name)+" decided to Stand in hand 1");

    def double(self):
        print(str(self.name)+" decided to Double in hand 1");
        self.bet = 2 * self.bet
        self.hit();

    def getHand2(self):
        print("");
        print("---" + str(self.name) + "'s second hand---");
        for i in range(len(self.hand2)):
                print(str(self.hand2[i]));
        print("Total: " + str(self.total2));
        if(self.blackjack2 == True):
            print("BLACKJACK");  

    def checkBlackjack2(self):
        if((self.hand[0] == 11 and self.hand[1] == 10) or (self.hand[0] == 10 and self.hand[1] == 11)):
            self.blackjack2 = True;
        else:
            self.blackjack2 = False;

    def hit2(self):
        index = random.randint(0, 12);
        card = self.cards[index]
        self.hand2.append(card);
        print(str(self.name)+" recieved a: " + str(card) + "in hand 2");

    def stand2(self):
        print(str(self.name)+" decided to Stand in hand 2");

    def double2(self):
        print(str(self.name)+" decided to Double in hand 2");
        self.bet2 = 2 * self.bet2
        self.hit2();     

    def options(self):
        while(self.isTurnOver == False):
            print("---" + str(self.name) + "'s 1st hand---")
            if(self.blackjack == True):
                print(str(self.name)+" got a blackjack");
                self.points += (self.bet + ((3/2)(self.bet)));
                print("Your 1st turn is over");
            elif(self.total < 21):
                print("Options for 1st hand:");
                print("Hit");
                print("Stand");
                if(self.total <= 11): ##double is possible
                    print("Double");
            elif(self.total == 21 and self.blackjack == False):
                print("Your 1st total is: " + str(self.total));
                print("Your 1st turn is over");
            else:
                print(str(self.name) + " bust");
                self.points = self.points - self.bet;
                print("Remaining points: " + str(self.points));
                print("Your 1st turn is over");
                
    def options2(self):
            while(self.isTurnOver2 == False):
                print("---" + str(self.name) + "'s 2nd hand---")
                if(self.blackjack2 == True):
                    print(str(self.name)+" got a blackjack");
                    self.points += (self.bet2 + ((3/2)(self.bet2)));
                    print("Your 2st turn is over");
                elif(self.total2 < 21):
                    print("Options for 2nd hand:");
                    print("Hit");
                    print("Stand");
                    if(self.total2 <= 11): ##double is possible
                        print("Double");
                elif(self.total2 == 21 and self.blackjack2 == False):
                    print("Your 2nd total is: " + str(self.total2));
                    print("Your 2nd turn is over");
                else:
                    print(str(self.name) + " bust");
                    self.points = self.points - self.bet2;
                    print("Remaining points: " + str(self.points));
                    print("Your 2nd turn is over");
