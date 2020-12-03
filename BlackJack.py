import random
import time

# creation of deck
cardfaces = []
suits = ["Hearts", "Spades", "Clubs", "Diamond"]
roylas = ["A", "J", "Q", "K"]
deck = []

for i in range(2, 11):
    cardfaces.append(i)
for j in roylas:
    cardfaces.append(j)
for items in suits:
    for ele in cardfaces:
        deck.append(str(ele) + f" [{items}]")
random.shuffle(deck)


# dealting cards
def DealtingCards(lst):
    lst.append(deck.pop(0))
    return lst


# calculate the score
def CalHand(lst):
    Aces = []
    noAces = []
    for ele in lst:
        if ele[0] == "A":
            Aces.append(ele)
        else:
            noAces.append(ele)
    Sum = 0
    for ele in noAces:
        if ele[0] in "JQK":
            Sum += 10
        elif int(ele[0]) in range(2,10):
            Sum += int(ele[0])
        elif ele[0:2] == "10":
            Sum += 10
    for ele in Aces:
        if Sum <= 10:
            Sum += 11
        else:
            Sum += 1
    return Sum

playerWallet = 5000

name = input("Enter your name : ")
print(f"Welcome {name.title()}! You have $ {playerWallet} in your wallet lets begin")

while True:
    print("""
    Chosse appropriate option
    1. Instruction
    2. Begin Game 
    3. Quit
    """)
    n = input("Choose : ")
    if n == "1":
        print("""
        WelCome to Casino Royale
        We will provide you with a wallet of $ 5000
        Rules:
        1. Each Bet is $ 500
        2. The bet can be doubled at anytime
        3. The bet can be surrendered at anytime
        4. in case of BlackJack you get 150% return
        5. you can quit anytime after the commenced hand is over
        """)
        time.sleep(10)
        continue

    elif n == "2":
        bonus = 0
        print(f"You have $ {playerWallet} in you wallet now")
        while True:
            if playerWallet < 500:
                print("You dont have enough funds to continue")
                quit()
            elif playerWallet < 0:
                print(f"You have a loan of $ {-1 * playerWallet} for which you will now have to settle via your belongings!!")
            print("A fresh hand begins")
            print(f"Player wallet : $ {playerWallet}")
            dealerCards = list()
            playerCards = list()
            dealerCards = DealtingCards(DealtingCards(dealerCards))
            playerCards = DealtingCards(DealtingCards(playerCards))
            print("Dealting the cards....")
            print()
            time.sleep(2)
            print(f"Player cards : {playerCards}")
            print(f"Dealer's Cards : [ Hidden, {dealerCards[1]}]")
            print()
            print("""
            Calculating the total score of the Player's cards
            Please wait....
            """)
            time.sleep(2)
            valuePlayer = CalHand(playerCards)
            print(f"Total score of Player : {valuePlayer}")

            if valuePlayer == 21:
                print("""
                    You have a BlackJack!!
                    Congartulations!! You Win the Hand
                    """)
                playerWallet += 750
                print("You have won $ 750")
                print(f"You have $ {playerWallet} in you wallet now")
                break

            elif valuePlayer > 21:
                print("""
                    Player is Busted
                    Dealer win s the round
                    """)
                playerWallet -= 500
                print(f"You have $ {playerWallet} in you wallet now")
                break

            print("""
                Do you wish to 
                1. Surrender
                2. Double the bet
                3. Continue with the bet
                """)
            time.sleep(1)
            decision = input("Chose : ")
            if decision == "1":
                print("Half the amount is returned to the Player wallet ($ 250)")
                playerWallet -= 250
                print(f"You have $ {playerWallet} in you wallet now")
                break
            elif decision == "2":
                print(f"The bet amount is doubled ($ 1000)")
                bonus = 500
            elif decision == "3":
                print("The bet amount is the same")


            while True:
                print("""
                    1. Stand : you are satisfied by your cards
                    2. Hit: You want more cards to improve your scores
                    """)
                choice = input("Make a Choice : ")
                if choice == "1":
                    print("Displaying Dealer's cards : ", dealerCards)
                    print("Calculating Score of Dealer...")
                    time.sleep(2)
                    valueDealer = CalHand(dealerCards)
                    print(f"Dealer's Score : {valueDealer}")
                    while True:
                        if valueDealer < 17:
                            print("Dealer's total is less than 17, Dealer will draw a card")
                            dealerCards = DealtingCards(dealerCards)
                            print(f"Dealer's New Cards : {dealerCards}")
                            valueDealer = CalHand(dealerCards)
                            print(f"New total Score of Dealer's Cards : {valueDealer}")
                            print()
                        else:
                            break
                    if valueDealer > 21:
                        print("""
                            Dealer has busted
                            Player wins the bet
                                        """)
                        playerWallet += 500 + bonus
                        print(f"You have $ {playerWallet} in you wallet now")
                        break

                    elif valuePlayer < valueDealer:
                        print("""
                            Dealer has a better hand
                            Dealer wins the bet
                                        """)
                        playerWallet -= (500 + bonus)
                        print(f"You have $ {playerWallet} in you wallet now")
                        break
                    elif valuePlayer == valueDealer:
                        print("Draw")
                        break

                elif choice == "2":
                    print("Drawing a card for Player......")
                    playerCards = DealtingCards(playerCards)
                    print(f"Player's New Cards : {playerCards}")
                    valuePlayer = CalHand(playerCards)
                    print(f"New total Score of Player's Cards : {valuePlayer}")
                    if valuePlayer > 21:
                        print("""
                        Player is Busted
                        Dealer wins
                            """)
                        playerWallet -= (500 + bonus)
                        print(f"You have $ {playerWallet} in you wallet now")
                        break

            break
    elif n == "3":
        break
    else:
        print("Invalid input. Choose again")
        time.sleep(1)
        continue
