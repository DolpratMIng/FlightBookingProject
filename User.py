class User:
    # def __init__(self, fName,lName,telephone,gender,nationality,bDate,email):
    fName = ""
    lName = ""
    telephone = ""
    gender = ""
    nationality = ""
    bDate = ""
    email = ""
    def start(self):
        self.fName = input("what is your name")
        self.lName = input("what is you last name")
        self.telephone = input("your number")
        self.gender = input("your Gender")
        self.nationality = input("your nationality")
        self.bDate = input("your birth day")
        self.email = input("your email")
    def toString(self):
        print(f"{self.fName} + {self.lName} + {self.telephone} + {self.gender} + {self.nationality} + {self.bDate} + {self.email}") 