from Airplane import Airplane
class Data:
    AirList = ["Hatyai","Bangkok"]
    def airlistPrint(self):
        for i in self.AirList:
            print(i,end=" ")
        print()

    # object of airplane
    airplane1 = Airplane("Air Asia", "FD3114", "8:00 AM", 1520)
    airplane2 = Airplane("Vietjet", "VD2554", "1:00 PM", 1340)
    airplane3 = Airplane("Lion Air", "LD1550", "9:00 PM", 2000)

    # list to store object of airplanee
    listplane = ["",airplane1, airplane2, airplane3]
    
