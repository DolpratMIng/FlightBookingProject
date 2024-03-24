import datetime
class Airplane:
    specific_time = datetime.time()
    def __init__(self,airline, name, time, price):
        self.airline = airline
        self.name = name
        self.time = time
        self.price = price
    def __str__(self):
        return f"Airline: {self.airline}\nName: {self.name}\nTime: {self.time}\nPrice: {self.price}\n"