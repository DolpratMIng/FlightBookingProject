from Airplane import *
from Airport import *

airplane1 = Airplane("Air Asia", "FD3114", "8:00 AM", 1520)
airplane2 = Airplane("Vietjet", "VD2554", "1:00 PM", 1340)
airplane3 = Airplane("Lion Air", "LD1550", "9:00 PM", 2000)


listplane = [airplane1, airplane2, airplane3]

airp1 = Airport()
airp1.start()

print(f"This is the available airlines on date: {airp1.date}")
for i in listplane:
    print(i)



