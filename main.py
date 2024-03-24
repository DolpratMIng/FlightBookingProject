from Airport import *
isTrue = True
AirList = ["Hatyai","Bangkok"]
while(isTrue):
    def start(self):
        for i in self.AirList:
            print(i,end=" ")
        print()
    date = input("enter you date in dd/mm/yy format: ")
    fromAir = input("from what airport do you wanna go?: ")
    toAir = input("to what airport you wanna go?: ")
    airport = Airport(fromAir,toAir,date)

    if(fromAir and toAir in AirList):
        airport.toString()
    else:
        print('there is no data of this')

