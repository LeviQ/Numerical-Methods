import math
import numpy as np

def Lagrange(x, xw, yw, n):

    ww = [0] * len(x)
    for k in range(len(ww)):
        suma = 0
        for i in range(len(xw)):
            ilocz = yw[i]
            for j in range(n+1):
                # print(j)
                if(i!=j):
                    ilocz *= ((x[k]-xw[j])/(xw[i]-xw[j]))
            suma += ilocz
        ww[k] = suma
    return ww

x = [1,3,6]

xw = [-2, 1, 4]
yw = [5, 3, 7]
n = 2

print(Lagrange(x, xw, yw, n))