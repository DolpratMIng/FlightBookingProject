from Airport import *
from Data import *
from User import *
from Card import *
from OnlineBanking import *
from Receipts import *
import random
x = random.randrange(10)   
isTrue = True
airport = Airport(isTrue)
user = User()
receipts = Receipt(airport.date,user.fName + user.lName)
while(isTrue):
    airport.start()#get airport data
    user.start()#get user data
    chooseBank = input("choose way to transaction (B) for online bank (C) for Card ")
    if(chooseBank == "B"):
        onlineBanking = OnlineBanking(100,x)
        onlineBanking.start()
    elif(chooseBank == "C"): 
        card = Card(100,x)
        card.start()
    else:
        print("error")
        break

    toStop = input("to exit press E to restart press R")
    if(toStop == "e"):
        isTrue = False

    

