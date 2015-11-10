from Aircraft import *

class Tower:
    __flightClearance = False
    flightList = ["0001a", '0001b', '0001c', '0001d', '0001e']
    flightNum = ""
    __fuelCheck = False
    # Testing airplane codes are correct and adding them to a list of correct codes.
    # Codes can be added also.

    def __init__(self):
        self.anAirplane = Aircraft()

    def currentFlightList(self):
        for plane in self.flightList:
            print(plane)

    def updateFlightList(self, flightNum):
        # testing new flight codes are of correct format
        while True:
            if len(flightNum) == 5:
                if flightNum not in self.flightList:
                    print("Flight code", flightNum, "does not appear to be on our system.")
                    self.add_to_system = input("Do you wish to be added to the updated system?")
                else:
                    print("Flight code", flightNum, " is in our system.")
                    break
                if self.add_to_system == "y":
                    self.flightList.append(flightNum)
                    self.currentFlightList()
                    break
                else:
                    print("Flight number not added to system.")
                    break



    # Checks flight codes are correct.
    def checkFlightList(self):
        print("")
        while True:
            for plane in self.flightList:
                print(plane)
            check = input("Flight list check correct?")
            if check == "y":
                print("Flight list authorization complete.")
                break
            else:
                removeFlight = input("Enter flight number that you wish to remove:")
                if removeFlight in self.flightList:
                    self.flightList.remove(removeFlight)
                    print("Flight number", removeFlight, "was deleted from flight list system.")
                else:
                    print("Invalid flight number entered.")
                    print("Please enter a authorized flight code.")

    def requestFlightCheck(self):
        self.anAirplane.flightNum = input("Enter flight number: ")
        if len(self.anAirplane.flightNum) == 5:
            if self.anAirplane.flightNum not in self.flightList:
                print("Flight code", self.anAirplane.flightNum, "does not appear to be on our system.")
                self.add_to_system = input("Do you wish to be added to the updated system?")
                if self.add_to_system == "y":
                    self.flightList.append(self.anAirplane.flightNum)
                    self.currentFlightList()
                else:
                    print("Flight number not added to system.")

            else:
                # Create anAirplane object and grant clearance
                print("Flight code", self.anAirplane.flightNum, "is in our system.")

                #check fuel
                self.anAirplane.fuelCheck()

                if self.__fuelCheck == False:
                    print("Refueling in process .. ")
                    self.anAirplane.addFuel(15000)
                    self.anAirplane.__flightClearance = self.anAirplane.fuelCheck()
                    self.anAirplane.preFlightCheck()
                else:
                    self.anAirplane.__flightClearance = self.anAirplane.fuelCheck()
                    self.anAirplane.preFlightCheck()




