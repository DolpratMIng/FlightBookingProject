from Payment import Payment

class OnlineBanking(Payment):
    def __init__(self,bankName):
        self.bankName = bankName