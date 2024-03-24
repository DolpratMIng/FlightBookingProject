from Airport import *
from Data import *
from User import *
airport = Airport()
user = User()
isTrue = True
while(isTrue):
    airport.start()
    User.start()
    airport.toString()
    user.toString()
    toStop = input("to exit press e to restart press r")
    if(toStop == "e"):
        isTrue = False

    

