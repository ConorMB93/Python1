from math import pi, sin, cos, acos

degrees_to_radians = 2 * pi / 360
r = 6371


# calculating the distance using latt long formula
def distance_cal(latt1, latt2, long1, long2):
    phi1 = (90 - latt1) * degrees_to_radians
    phi2 = (90 - latt2) * degrees_to_radians
    theta1 = long1 * degrees_to_radians
    theta2 = long2 * degrees_to_radians
    dist1 = acos((sin(phi1) * sin(phi2) * cos(theta1 - theta2)) + cos(phi1) * cos(phi2)) * r
    return dist1

# finding distance between to airports inputted my user
def distance_cities(city1, city2):
    airport_list = ["DUB", "LHR", "JFK", "AAL", "CDG", "SYD"]
    latt_list = [53.421333, 51.4775, 40.639751, 57.092789, 49.012779, -33.9461111]
    long_list = [-6.270075, -.461389, -73.778925, 9.849164, 2.55, 151.177222]

    idx = airport_list.index(city1)
    jdx = airport_list.index(city2)

    latt1 = latt_list[idx]
    long1 = long_list[idx]
    latt2 = latt_list[jdx]
    long2 = long_list[jdx]

    dist = distance_cal(latt1, long1, latt2, long2)
    return dist


def main():
    table_list = []
    # add values to a table list
    while len(table_list) < 18:
        city1 = raw_input("Enter first airport: ")
        city2 = raw_input("Enter second city: ")
        dist = distance_cities(city1, city2)
        # checking to see if inputs are already in table list
        if city1 not in table_list or city2 not in table_list:
            table_list.append(city1)
            table_list.append(city2)
            table_list.append(dist)
            print(table_list)

        else:
            print("You have already added these Airports to the table_list.")
            print("Please enter new Airports from Table 1.")
            None


main()
