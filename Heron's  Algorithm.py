import numpy as np

### Calculation of the sqr using Heron's Algorithm
def Herons_Algorithm(a,x,eps):

    b = 1
    if(a > 0):
        while (x - b > eps):
            x = (x + b) / 2
            b = a / x
        return x
    else:
        print("Can't get a square root from a negative number")     ### Exception

if(type(Herons_Algorithm(25, 25, 0.000001)) is float):
    print("Square root is: ",round(Herons_Algorithm(25, 25, 0.00001), 5))
    print(" ")
