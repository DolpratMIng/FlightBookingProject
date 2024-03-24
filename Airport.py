from Data import *
data = Data()
class Airport:
    date = 0
    fromAir = ""
    toAir = ""
    def start(self):
        self.date = input("enter you date in dd/mm/yy format: ")
        data.airlistPrint()
        self.fromAir = input("from what airport do you wanna go?: ")
        self.toAir = input("to what airport you wanna go?: ")

    def toString(self):

        if(self.fromAir and self.toAir in data.AirList):
            print(f"from {self.fromAir} to {self.toAir} the date is {self.date} ")
        else:
            print('there is no data of this')
        
        



    