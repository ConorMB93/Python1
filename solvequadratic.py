# solve quadratic. Will take three inputs , a , b and c. Use -b forumla. Test for imaginary roots.

from math import sqrt


# testing for real/ imag roots
def disc(a, b, c):
    d = (b ** 2) - 4 * a * c

    if d == 0:
        print("One root is real (double root).")
        double_root1 = quad1(a, b, c)
        double_root2 = quad1(a, b, c)
        print(double_root1, double_root2)

    elif d > 0:
        print("Both roots are real.")
        root1 = quad1(a, b, c)
        root2 = quad2(a, b, c)
        print(root1, root2)

    elif d < 0:
        print("Both roots are complex.")
        solve_comp1 = complex(quad1(a, b, c))
        solve_comp2 = complex(quad2(a, b, c))
        print(solve_comp1, solve_comp2)
    else:
        print("Error. Try again.")
        main()


# use to solve
def quad1(a, b, c):
    ans_pos = - b + (sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    return ans_pos


def quad2(a, b, c):
    ans_neg = - b - (sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    return ans_neg


def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    disc(a, b, c)


main()
