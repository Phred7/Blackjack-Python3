##for next version consider using a dictionary for each hand so total, is callable... will allow simpler methods in the long run

import random

class BlackjackSplit():
    def __init__(self, name, hand, bet, balance):
        self.name = name;
        self.bet = self.bet2 = bet;
        self.hand = [];
        self.hand2 = [];
        hands = hand[0];
        self.hand.append(hands);
        self.hand2.append(hands);
        self.total = self.total2 = 0;
        self.points = balance;
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
        self.isTurnOver = self.isTurnOver2 = False;
        self.blackjack = self.blackjack2 = False;
        self.bust = self.bust2 = False;
        self.play();

##---------------------------------------------------------------------

    def getCard(self, hand):
        index = random.randint(0, 12);
        card = self.cards[index]
        hand.append(card)

    def deal(self):
        self.getCard(self.hand);
        self.getCard(self.hand2);
        self.blackjack = self.checkBlackjack(self.hand);
        self.blackjack2 = self.checkBlackjack(self.hand2);

    def getHands(self):
        self.total = self.updateTotal(self.hand);
        self.total2 = self.updateTotal(self.hand2);
        return self.total, self.total2;

    def printHands(self):
        self.getHands();
        self.printHand(self.hand, self.total, self.blackjack, 1);
        self.printHand(self.hand2, self.total2, self.blackjack2, 2);

    def getTotals(self):
        return [self.total, self.total2];

    def getBets(self):
        return [self.bet, self.bet2];

    def getBusts(self):
        return [self.bust, self.bust2];

    def getBlackjacks(self):
        return [self.blackjack, self.blackjack2];

    def getTotal(self, numHand):
        if(numHand == 1):
            return self.total;
        else:
            return self.total2;

    def getBet(self, numHand):
        if(numHand == 1):
            return self.bet;
        else:
            return self.bet2;
        
    def getBust(self, numHand):
        if(numHand == 1):
            return self.bust;
        else:
            return self.bust2;

    def getBlackjack(self, numHand):
        if(numHand == 1):
            return self.blackjack;
        else:
            return self.blackjack2;

    def options(self):
        self.total, self.bet, self.isTurnOver, self.bust = self.option(self.hand, self.bet, self.isTurnOver, self.blackjack, 1);
        self.total2, self.bet2, self.isTurnOver2, self.bust2 = self.option(self.hand2, self.bet2, self.isTurnOver2, self.blackjack2, 2);

    def calculate(self, houseBust, houseTotal):
        self.calculateHand(houseBust, houseTotal, 1);
        self.calculateHand(houseBust, houseTotal, 2);
        
##---------------------------------------------------------------------

    def printHand(self, hand, total, blkjBool, numHand):
        print("");
        print("---" + str(self.name) + "'s hand: " + str(numHand)+ "---");
        for i in range(len(hand)):
                print(str(hand[i]));
        print("Total: " + str(total));
        if(blkjBool == True):
            print("BLACKJACK");

    def getAces(self, hand):
        aces = 0;
        for i in range(len(hand)):
            if(hand[i] == 11):
                aces += 1;
        return aces;

    def updateTotal(self, hand):
        total = 0;
        for i in range(len(hand)):
                total += hand[i];
        return total;

    def checkBlackjack(self, hand):
        if((hand[0] == 11 and hand[1] == 10) or (hand[0] == 10 and hand[1] == 11)):
            blkjBool = True;
        else:
            blkjBool = False;
        return blkjBool;

##---------------------------------------------------------------------

    def hit(self, hand, numHand):
        self.getCard(hand);
        card = hand[-1];
        print(str(self.name)+" decided to hit and recieved a: " + str(card) + " in hand: " + str(numHand));
        
    def stand(self):
        turn = True ##isTurnOver = True
        return turn;

    def double(self, hand, bet):
        bet += bet
        self.hit(hand);
        turn = True; ##isTurnOver = True
        return turn, bet;

    def option(self, hand, bet, turn, blkjBool, numHand):
        while(turn == False):
            total = self.updateTotal(hand);
            aces = self.getAces(hand);
            print("\n---" + str(self.name) + "'s hand: " +str(numHand) + "---")
            print("Hand" + str(hand));
            print("Total " +str(total));
            if(blkjBool == True):
                print(str(self.name)+" got a blackjack");
                turn = True;
                print("Your 1st turn is over");
            elif(total > 21 and aces > 0):
                total += -10;
                for i in range(len(hand)):
                    if(hand[i] == 11):
                        hand[i] = 1;
                        break;
            elif(total < 21):
                choice = 0;
                while(choice == 0):
                    print("Options:");
                    print("1. Hit");
                    print("2. Stand");
                    if(total <= 11): ##double is possible
                        print("4. Double");
                    choice = int(input("Your choice: "));
                    if(choice == 1):
                        self.hit(hand, numHand);
                    elif(choice == 2):
                        turn = self.stand();
                        print(str(self.name)+" decided to Stand in hand: " + str(numHand));
                    elif(self.total <= 11 and choice == 4):
                        print(str(self.name)+" decided to Double in hand: " + str(numHand));
                        turn, bet = self.double(hand, bet);
                    else:
                        choice = 0;
                        print("That option is invalid. Try again:");
            elif(total == 21 and blkjBool == False):
                print("Your total is: " + str(total));
                turn = True;
            else:
                turn = True;
        total = self.updateTotal(hand);
        self.printHand(hand, total, blkjBool, numHand);
        if(total == 21 and self.blackjack == False):
            print("Your total is: " + str(total));
            print(str(self.name) + "'s turn #" + str(numHand) + " is over");
            bust = False;
        elif(total > 21):
            print(str(self.name) + " bust");
            print(str(self.name) + "'s turn #" + str(numHand) + " is over");
            bust = True;
        else:
            bust = False;
            print(str(self.name) + "'s turn #" + str(numHand) + " is over");
        return total, bet, turn, bust;

##---------------------------------------------------------------------
    
    def win(self, bet, numHand):
        self.points += bet;
        print(str(self.name) + "'s hand #" + str(numHand) +  " won " + str(bet) + "points. Total: " + str(self.points) + "points.");

    def lost(self, bet, numHand):
        self.points += -bet;
        print(str(self.name) + "'s hand #" + str(numHand) +  " lost. Remaining points: " + str(self.points));
        
    def _bust(self, bet, numHand):
        self.points += -bet;
        print(str(self.name) + "'s hand #" + str(numHand) +  " bust. Remaining points: " + str(self.points));

    def _blackjack(self, bet, numHand):
        blkjackIncrease = 0;
        blkjackIncrease = bet + int(((3/2)*(bet)))
        self.points += blkjackIncrease;
        print(str(self.name) + "'s hand #" + str(numHand) + " got a blackjack and won " + str(blkjackIncrease) + "points. Total: " + str(self.points) + "points.");

##---------------------------------------------------------------------
        
    def calculateHand(self, houseBust, houseTotal, numHand):
        if(self.getBlackjack(numHand) == True):
            self._blackjack(self.getBet(numHand), numHand);
        elif(self.getBust(numHand) == True):
            self._bust(self.getBet(numHand), numHand);
        elif(houseBust == True):
            if(self.getBust(numHand) == False):
                self.win(self.getBet(numHand), numHand);
            else:
                self.lost(self.getBet(numHand), numHand);
        elif(houseBust == False):
            if(self.getTotal(numHand) >= houseTotal):
                self.win(self.getBet(numHand), numHand);
            else:
                self.lost(self.getBet(numHand), numHand);
        else:
            print("else - final");
    
##---------------------------------------------------------------------
        
    def play(self):
        self.deal();
        self.printHands();
        self.options();
        ##self.calculate(False, 19);

##def main():
##    test = BlackjackSplit_("Ted", [10, 10], 150, 1500);
##
##main();
