# harmonic series

def harmonic(n):
    total = 0.0
    for i in range (1, n+1):

    #must have range of (2, n) otherwise division by zero error

        total += (1.0 / (i**2))
    return total

def main():
    n = int(input("Enter a value for n: "))
    total = harmonic(n)
    print(total)

main()
