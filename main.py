from Airport import *
from Data import *
airport = Airport()
isTrue = True
while(isTrue):
    airport.start()
    airport.toString()
    toStop = input("to exit press e to restart press r")
    if(toStop == "e"):
        isTrue = False

    

