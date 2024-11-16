import os
def bid_comparer(bid):
    bidWinner,winner=0,""
    for i in bid:
        bidPrice=bid[i]
        if bidWinner<bidPrice :
            bidWinner=bidPrice
            winner=i
    else :
        print(f"The winner of this auction is {winner} with {bidWinner} ")
run =True
bid={}
while run :
    os.system('cls')
    name=input("What is your name ?\n")
    bidAmt=float(input("How much you want to bid ?\n"))
    bid[name]=bidAmt
    bidders=input("If there are any other bidders type yes if not no ")
    if bidders=="yes":
        run=True
    elif bidders=="no":
        bid_comparer(bid)
        run=False
    else :
        print("Wrong input\nThe auction is stopped")
        run = False 