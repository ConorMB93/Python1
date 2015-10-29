'''
******************
*                *
* FIBONACCI      *
*                *
* by Conor Byrne *
*                *
******************

'''
import time

def fibonacci(n):
    currNum = 1
    prevNum = 0
    count = 0
    print(currNum)
    while True:
        count += 1
        if count <= n:

            fib = currNum + prevNum
            prevNum = currNum
            currNum = fib
            print(fib)

        else:
            break


def main():

    n = int(input("How many Fibonacci numbers do you wish to generate? "))
    print("")
    print("Fibonacci sequence up to", n, " numbers is: ")
    start = time.clock() # processor time
    fibonacci(n)
    stop = time.clock()
    elapsed = stop - start
    print("")
    print("Total time to complete program: ", elapsed)


main()
