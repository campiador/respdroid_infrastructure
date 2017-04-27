import math


class QuadraticTest:
    def first_function(self):
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))

        if (a == 0):
            print("in a quadratic equation, a should be non-zero")
            exit(1)


        delta = b ** 2 - 4 * a * c

        if (delta < 0):
            print("delta is {}, but should be greater than 0. Please enter valid numbers.".format(delta))
            exit(1)
        delta_sqrt = math.sqrt(delta)

        root1 = (-b + delta_sqrt) / (2 * a)
        root2 = (-b - delta_sqrt) / (2 * a)

        print("first root = {}, and second root = {}".format(root1, root2))

QuadraticTest().first_function()