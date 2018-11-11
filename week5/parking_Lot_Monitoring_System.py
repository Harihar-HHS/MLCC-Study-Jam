'''
Design and Implement a parking lot monitoring system using OOPs concepts in Python.

Imagine an parking lot with 20 parking spaces, where each parking space has an ID which is a natural number, starting with 1, 2, 3, ….upto 20. Parking space '1' is the one closest to the entrance.
The parking space can be in three sizes: small(10 parking spaces), medium(7 parking spaces) and large slots(3 parking spaces).
Three types of vehicles are allowed to be parked in a parking space: motorcycle(small), car(medium) and bus(large)
        A motorcycle can be parked in any small, medium or large parking spaces.
        A car can be parked in either a medium slot or a large parking spaces.
        A bus can be parked only in a large parking space.
When a user enters the parking lot, vehicle type and vehicle ID are noted and fed as input to our system
Our system should assign the vehicle to the nearest parking space available(if any parking space is available)
User should be given a printed ticket with the assigned parking spot ID and his vehicle ID
'''


# Assuming parking slots 1-10 = small vehicles (bikes)
#                        11-17 = medium vehicles (cars)
#                        18-20 = large vehicles (buses)


sv=0
mv=0
lv=0

ss=10
ms=7
ls=3

class vehicle(self):
    def __init__(self,id,type,slot):
        self.vid=id
        self.type=type
        self.slot=slot

class slot(vehicle):
    def __init__(self,slot,id,type):
        self.slot=slot
        self.vid=id
        super.__init__()
        
