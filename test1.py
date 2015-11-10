from Aircraft import *
from tower import *

myAirplane = Aircraft()
myAirplane.addFuel(500)
myAirplane.printStatus()
myAirplane.takeOff()
print("---")
dublinTower = Tower()
dublinTower.requestFlightCheck()
