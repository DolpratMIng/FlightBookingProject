from Airplane import Airplane2
from Airport import *
from Data import *

# from Data
data = Data()

# Airport
airp1 = Airport()
airp1.start()

# Airplane
airplanefunction = Airplane2()

# print(f"Choose the airlines available on date: {airp1.date}")
airplanefunction.airlines_answer(airp1.date, data.listplane)
# for i in data.listplane:
#     print(i)



