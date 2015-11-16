'''

Airports
by Conor Byrne

'''


class Airports:
    def __init__(self, airport_code, name, city, country, lat, long):
        self.airport_code = airport_code
        self.name = name
        self.country = country
        self.city = city
        self.lat = float(lat)
        self.long = float(long)

    def __str__(self):
        return " {} ( Name : {} , {} ,{} lat :{} long :{}) ". format(
            self.airport_code, self.name, self.city, self.country, self.lat, self.long)


def main():
    myAirport = Airports("DUB", "Dublin Airport","Dublin", "Ireland", 15, 23)
    print(myAirport)

if __name__ == "__main__":
    main()
