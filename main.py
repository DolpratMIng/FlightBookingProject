from Airport import *
from Data import *
from User import *
from Card import *
from OnlineBanking import *
airport = Airport()
user = User()
onlineBanking = OnlineBanking()
card = Card()
isTrue = True
while(isTrue):
    airport.start()
    User.start()
    chooseBank = input("choose way to transaction (B) for online bank (C) for Card ")
    if(chooseBank == "B"):
        onlineBanking.start()
    elif(chooseBank == "C"): 
        card.start()
    else:
        print("error")
    toStop = input("to exit press E to restart press R")
    if(toStop == "e"):
        isTrue = False

    

