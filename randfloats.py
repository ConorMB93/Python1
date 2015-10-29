'''
******************
*                *
* randfloats     *
*                *
* by Conor Byrne *
*                *
******************
'''

import random

def randFloats(n, a, b):
    print("")
    count = 0
    while True:
        if count < n:
            count += 1
            randNum = random.uniform(a, b) # selects random float from interval
            print(randNum)
        else:
            break


def main():
    print("")
    print("*** RANDOM FLOAT GENERATOR ***")
    print("")
    n = int(input("How many random floats do you wish to generate? "))
    a = float(input("Enter the value of float 'a': "))
    b = float(input("Enter the value of float 'b': "))
    randFloats(n, a, b)



main()
