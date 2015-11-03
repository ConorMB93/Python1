'''

Circle Class
By Conor Byrne

'''

from math import pi

class Circle:
    def __init__(self):
        self.circ()

    def circ(self):
        r = float(input("Enter a radius value: "))
        self.value = 2 * pi * r

    def __str__(self):
        return str(self.value)


def main():
    n = int(input("How many circles do you wish to generate? "))
    count = 1
    while True:
        if count <= n:
            count += 1
            circle1 = Circle()
            print "This circle has an area of: ", circle1.value

        else:
            break


main()
