import random

class BlackjackSplit():
    def __init__(self, name, hand, bet, balance):
        self.name = name;
        self.bet = self.bet2 = bet;
        self.hand = []
        self.hand2 = []
        hands = hand[0]
        self.hand.append(hands);
        self.hand2.append(hands);
        self.total = 0;
        self.total2 = 0;
        self.points = balance;
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
        self.isTurnOver = False;
        self.isTurnOver2 = False;
        self.blackjack = False;
        self.blackjack2 = False;
        self.bust = False;
        self.bust2 = False;
##        print("\n\n" + str(hand[0]) + "\n\n");
##        print("\n\n" + str(self.hand[:]) + "\n\n");
##        print("\n\n" + str(self.hand2[:]) + "\n\n");
        self.deal();
        self.getHand();
        self.getHand2();
        self.options();
        self.options2();
        
    def getCard(self):
        index = random.randint(0, 12);
        card = self.cards[index]
        return card;

    def deal(self):
        card = self.getCard();
        self.hand.append(card);
        card2 = self.getCard();
        self.hand2.append(card2);

    def getHands(self):
        self.updateTotal();
        self.updateTotal2();
        return [self.total, self.total2];

##---------------------------------------------------------------------
        
    def getHand(self):
        self.updateTotal();
        print("");
        print("---" + str(self.name) + "'s first hand---");
        for i in range(len(self.hand)):
                print(str(self.hand[i]));
        print("Total: " + str(self.total));
        if(self.blackjack == True):
            print("BLACKJACK");

    def getAces(self):
        self.aces = 0;
        for i in range(len(self.hand)):
            if(self.hand[i] == 11):
                self.aces += 1;

    def getTotal(self):
        return self.total;

    def updateTotal(self):
        self.total = 0;
        for i in range(len(self.hand)):
                self.total += self.hand[i];

    def checkBlackjack(self):
        if((self.hand[0] == 11 and self.hand[1] == 10) or (self.hand[0] == 10 and self.hand[1] == 11)):
            self.blackjack = True;
        else:
            self.blackjack = False;
    
    def hit(self):
        index = random.randint(0, 12);
        card = self.cards[index]
        self.hand.append(card);
        print(str(self.name)+" recieved a: " + str(card) + " in hand 1");

    def stand(self):
        print(str(self.name)+" decided to Stand in hand 1");
        self.isTurnOver = True

    def double(self):
        print(str(self.name)+" decided to Double in hand 1");
        self.bet += self.bet
        self.hit();
        self.isTurnOver = True

    def options(self):
        while(self.isTurnOver == False):
            self.updateTotal();
            self.getAces();
            print("\n---" + str(self.name) + "'s 1st hand---")
            print("Hand" + str(self.hand));
            print("Total " +str(self.total));
            if(self.blackjack == True):
                print(str(self.name)+" got a blackjack");
                self.isTurnOver = True;
                print("Your 1st turn is over");
            elif(self.total > 21 and self.aces > 0):
                self.total += -10;
                for i in range(len(self.hand)):
                    if(self.hand[i] == 11):
                        self.hand[i] = 1;
                        break;
            elif(self.total < 21):
                choice = 0;
                while(choice == 0):
                    print("Options:");
                    print("1. Hit");
                    print("2. Stand");
                    if(self.total <= 11): ##double is possible
                        print("4. Double");
                    choice = int(input("Your choice: "));
                    if(choice == 1):
                        self.hit();
                    elif(choice == 2):
                        self.stand();
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
            print("Your first turn is over");
            self.bust = False;
        elif(self.total > 21):
            print(str(self.name) + " bust");
            print("Your first turn is over");
            self.bust = True;
        else:
            self.bust = False;
            print("Your first turn is over");


##---------------------------------------------------------------------

    def getHand2(self):
        self.updateTotal2();
        print("");
        print("---" + str(self.name) + "'s second hand---");
        for i in range(len(self.hand2)):
                print(str(self.hand2[i]));
        print("Total: " + str(self.total2));
        if(self.blackjack2 == True):
            print("BLACKJACK");

    def getAces2(self):
        self.aces2 = 0;
        for i in range(len(self.hand2)):
            if(self.hand2[i] == 11):
                self.aces2 += 1;

    def getTotal2(self):
        return self.total2;

    def updateTotal2(self):
        self.total2 = 0;
        for i in range(len(self.hand2)):
                self.total2 += self.hand2[i];

    def checkBlackjack2(self):
        if((self.hand2[0] == 11 and self.hand2[1] == 10) or (self.hand2[0] == 10 and self.hand2[1] == 11)):
            self.blackjack2 = True;
        else:
            self.blackjack2 = False;

    def hit2(self):
        index2 = random.randint(0, 12);
        card2 = self.cards[index2]
        self.hand2.append(card2);
        print(str(self.name)+" recieved a: " + str(card2) + " in hand 2");

    def stand2(self):
        print(str(self.name)+" decided to Stand in hand 2");
        self.isTurnOver2 = True

    def double2(self):
        print(str(self.name)+" decided to Double in hand 2");
        self.bet2 += self.bet2
        self.hit2();
        self.isTurnOver2 = True

    def options2(self):
        while(self.isTurnOver2 == False):
            self.updateTotal2();
            self.getAces2();
            print("\n---" + str(self.name) + "'s 2nd hand---")
            print("Hand2" + str(self.hand2));
            print("Total2 " +str(self.total2));
            if(self.blackjack2 == True):
                print(str(self.name)+" got a blackjack");
                self.isTurnOver2 = True;
                print("Your second turn is over");
            elif(self.total2 > 21 and self.aces2 > 0):
                self.total2 += -10;
                for i in range(len(self.hand2)):
                    if(self.hand2[i] == 11):
                        self.hand2[i] = 1;
                        break;
            elif(self.total2 < 21):
                choice = 0;
                while(choice == 0):
                    print("Options:");
                    print("1. Hit");
                    print("2. Stand");
                    if(self.total2 <= 11): ##double is possible
                        print("4. Double");
                    choice = int(input("Your choice: "));
                    if(choice == 1):
                        self.hit2();
                    elif(choice == 2):
                        self.stand2();
                    elif(self.total2 <= 11 and choice == 4):
                        self.double2();
                    else:
                        choice = 0;
                        print("That option is invalid. Try again:");
            elif(self.total2 == 21 and self.blackjack2 == False):
                print("Your total is: " + str(self.total2));
                self.isTurnOver2 = True;
            else:
                self.isTurnOver2 = True;
        self.updateTotal2();
        self.getHand2();
        if(self.total2 == 21 and self.blackjack2 == False):
            print("Your total is: " + str(self.total2));
            print("Your second turn is over");
            self.bust2 = False;
        elif(self.total2 > 21):
            print(str(self.name) + " bust");
            print("Your second turn is over");
            self.bust2 = True;
        else:
            self.bust2 = False;
            print("Your second turn is over");

##---------------------------------------------------------------------
                    
    def getBust(self):
        return self.bust;

    def getBlackjack(self):
        return self.blackjack;
    
    def win(self):
        self.points += self.bet;
        print(str(self.name) + "'s 1st hand won " + str(self.bet) + "points. Total: " + str(self.points) + "points.");

    def lost(self):
        self.points += -self.bet;
        print(str(self.name) + "'s 1st hand lost. Remaining points: " + str(self.points));
        
    def _bust(self):
        self.points += -self.bet;
        print(str(self.name) + "'s 1st hand bust. Remaining points: " + str(self.points));

    def _blackjack(self):
        self.blkjackIncrease = self.bet + int(((3/2)(self.bet)))
        self.points += self.blkjackIncrease;
        print(str(self.name) + "'s 1st hand got a blackjack and won " + str(self.blkjackIncrease) + "points. Total: " + str(self.points) + "points.");

##---------------------------------------------------------------------
                    
    def getBust2(self):
        return self.bust2;

    def getBlackjack2(self):
        return self.blackjack2;
    
    def win2(self):
        self.points += self.bet2;
        print(str(self.name) + "'s 2nd hand won " + str(self.bet2) + "points. Total: " + str(self.points) + "points.");

    def lost2(self):
        self.points += -self.bet2;
        print(str(self.name) + "'s 2nd hand lost. Remaining points: " + str(self.points));
        
    def _bust2(self):
        self.points += -self.bet2;
        print(str(self.name) + "'s 2nd hand bust. Remaining points: " + str(self.points));

    def _blackjack2(self):
        self.blkjackIncrease2 = self.bet + int(((3/2)(self.bet)))
        self.points += self.blkjackIncrease2;
        print(str(self.name) + "'s 2nd hand got a blackjack and won " + str(self.blkjackIncrease2) + "points. Total: " + str(self.points) + "points.");

##---------------------------------------------------------------------
        
    def calculate(self, houseBust, houseTotal):
        if(self.getBlackjack() == True):
            self._blackjack();
        elif(self.getBust() == True):
            self._bust();
        elif(houseBust == True):
            if(self.getBust() == False):
                self.win();
            else:
                self.lost();
        elif(houseBust == False):
            if(self.getTotal() >= houseTotal):
                self.win();
            else:
                self.lost();
        else:
            print("else - final");

        if(self.getBlackjack2() == True):
            self._blackjack2();
        elif(self.getBust2() == True):
            self._bust2();
        elif(houseBust == True):
            if(self.getBust2() == False):
                self.win2();
            else:
                self.lost2();
        elif(houseBust == False):
            if(self.getTotal2() >= houseTotal):
                self.win2();
            else:
                self.lost2();
        else:
            print("else - final");
            
        return self.points
    
