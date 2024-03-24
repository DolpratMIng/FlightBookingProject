import datetime
class Payment:
    #attribute  
    timeForPayment = datetime.datetime.now()
    def __init__(self, price, refNo,):
        self.price = price
        self.refNo = refNo
    
    #to find the final amount
    def toString(self):
        print(f"{self.price} + {self.refNo} + {self.timeForPayment}")