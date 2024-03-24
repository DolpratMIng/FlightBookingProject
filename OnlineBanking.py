from Payment import Payment
from Data import *
data  = Data()
class OnlineBanking(Payment):
    # def __init__(self,bankName):
    #     self.bankName = bankName
    bankName = 0
    def start(self):
        data.bankPrint()
        self.bankName = input

