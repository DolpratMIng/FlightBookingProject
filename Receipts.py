

class Receipt:
    def __init__(self, date, ticketNumber, bookingNumber,userName,):
       self.date = date
       self.ticketNumber = ticketNumber
       self.bookingNumber = bookingNumber
       self.userName = userName
    def toString(self):
        print(f"{self.date}\n{self.ticketNumber}\n{self.bookingNumber}\n{self.userName}")


       