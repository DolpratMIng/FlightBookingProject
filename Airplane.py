class Airplane:

    # Class attribute to keep track of the count
    count = 0
    def __init__(self,airline, name, time, price):
        self.airline = airline
        self.name = name
        self.time = time
        self.price = price
        # Increment the count and assign it to the 'number' attribute
        Airplane.count += 1
        self.number = Airplane.count

    def __str__(self):
        return f"Number: {self.number}\nAirline: {self.airline}\nName: {self.name}\nTime: {self.time}\nPrice: {self.price}THB\n"