class Aircraft:
    __fuel = 0  # private attribute containing current fuel in aircraft
    maxFuel = 24000
    __fuelCheck = False  # this is a Boolean flag for a pre-flight check.
    MIN_FUEL = 1000  # minimum amount of fuel for takeoff
    __flightClearance = False
    flightNum = ""

    def __init__(self, planeType="747"):
        self.planeType = planeType

    def setFlightNum(self, flightNum):
        self.flightNum = flightNum

    def fuelCheck(self):
        if self.__fuel < self.MIN_FUEL:
            print("Fuel Check Failed: Current fuel below safe limit:", self.__fuel,
                  " less than ", self.MIN_FUEL)
            self.__fuelCheck = False
        else:
            print("Fuel Check Complete:", self.__fuel)
            self.__fuelCheck = True

    def takeOff(self):
        if self.__fuelCheck == True:
            print("Cleared for Takeoff! Fasten your seat-belt!")
        else:
            print("Take off Failed: Please complete pre-flight check first")
            print(self.fuelCheck())

    def printStatus(self):
        print("Current fuel:", self.__fuel)

    def addFuel(self, volume):
        unusedFuel = 0

        if volume < 0:
            print("No syphoning fuel!")
        elif self.__fuel + volume <= self.maxFuel:
            self.__fuel = self.__fuel + volume
        elif self.__fuel + volume > self.maxFuel:
            self.__fuel = self.maxFuel
            unusedFuel = volume - self.__fuel

        return unusedFuel

    def preFlightCheck(self):
        if self.__fuelCheck == False:
            self.__flightClearance = False
            print("DANGER!! DO NOT TAKE OFF!. You are not authorized for clearance!")

        else:
            self.__flightClearance = True
            print("Clearance authorized. You can proceed!")
            self.takeOff()
