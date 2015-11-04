"""

Norm of a given vector
By Conor Byrne

"""

from math import sqrt


class Vector:
    def __init__(self):
        self.vect()

    def vect(self):
        x = float(input("Enter 'x' value: "))
        y = float(input("Enter 'y' value: "))
        self.norm = sqrt((x ** 2) + (y ** 2))

    def __str__(self):
        return str(self.norm)


def main():
    norm1 = Vector()
    print(norm1)


main()
