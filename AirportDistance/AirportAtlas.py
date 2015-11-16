"""

AirportAtlas
by Conor Byrne

"""

from Airports import *
from math import pi, sin, cos, acos
import csv

class AirportAtlas:
    filname = "airport(1).csv"

    def __init__(self, airport_file=filname):
        self.airports = self.loadData(airport_file)

    """
    Opens csv file containing Airport info.
    """
    def loadData(self, airport_file):
        dict = {}
        with open(airport_file, "rt") as f:
            csvfilelines = list(csv.reader(f))  # stores each line of csv as list
            for row in csvfilelines:
                try:
                    dict[row[4]] = Airports(row[4], row[1], row[3], row[2], row[6], row[7])

                except KeyError:  # Skips if error found and continues with loop
                    continue
        return dict

    """
    Prints out dictionary as list as cannot iterate
    through items in dictionary.
    """
    def printDict(self):
        myAtlas = list(self.airports.values())
        for row in myAtlas:
            try:
                print(row)
            except TypeError:
                continue

    """
    User can access info about Airport they input.
    """
    def getAirport(self, airport_code):
        try:
            print(self.airports[airport_code.upper()])
            print("-----")
            return self.airports[airport_code.upper()]
        except KeyError:
            None

    """
    Calculates distance between Airports.
    """
    @staticmethod
    def getDistanceFormula(lat1, lat2, long1, long2):
        print("Coordinates for Airport1:", lat1, long1)
        print("Coordinates for Airport2:", lat2,long2)
        degrees_to_radians = 2 * pi / 360
        r = 6371
        phi1 = (90 - lat1) * degrees_to_radians
        phi2 = (90 - lat2) * degrees_to_radians
        theta1 = long1 * degrees_to_radians
        theta2 = long2 * degrees_to_radians
        distanceCal = acos((sin(phi1) * sin(phi2) * cos(theta1 - theta2)) + cos(phi1) * cos(phi2)) * r
        print("-----")
        return print("Distance =", distanceCal)

    """
    Gets latitudes and longitudes of Airports from Airport objects.
    """
    def getLatLong(self, code1, code2):
        code1 = self.getAirport(code1)
        code2 = self.getAirport(code2)
        distance = AirportAtlas.getDistanceFormula(code1.lat, code2.lat, code1.long, code2.long)
        return distance

def main():
    myAirportAtlas = AirportAtlas()
    myAirportAtlas.loadData(airport_file="airport(1).csv")
    myAirportAtlas.getLatLong(code1="DUB", code2="JFK")

if __name__ == "__main__":
    main()
