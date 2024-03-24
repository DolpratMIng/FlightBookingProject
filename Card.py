from Payment import Payment
from Data import *
data = Data()
class Card(Payment):
    # def __init__(self, type, nameOnCard, numberOnCard, CW):
    #     self.type = type # VISA or Mastercard
    #     self.nameOnCard = nameOnCard
    #     self.numberOnCard = numberOnCard
    #     self.CW = CW
    def start(self):
        data.cardPrint;
        self.type = type # VISA or Mastercard
        self.nameOnCard = input("name of the owner of the card")
        self.numberOnCard = input("put your number of the card")
        self.CW = input("put your cw on the card")