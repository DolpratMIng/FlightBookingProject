import datetime
x = datetime.datetime.now()
class Payment:
    #attribute
    def __init__(self, price, refNo):
        self.price = price
        self.refNo = refNo
    
    # Local Date
    def booking_Date(self):
        self.date = datetime.datetime.now()
        print(self.date)

    #to find the final amount
    def amount():
        pass
