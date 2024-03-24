from Payment import Payment

class Card(Payment):
    def __init__(self, type, nameOnCard, numberOnCard, CW):
        self.type = type # VISA or Mastercard
        self.nameOnCard = nameOnCard
        self.numberOnCard = numberOnCard
        self.CW = CW