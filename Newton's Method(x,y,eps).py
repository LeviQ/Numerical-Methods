from scipy.misc import derivative
from numpy import linalg as la
import matplotlib.pyplot as plt
import numpy
import numpy as np


def function1(x,y):
    return x**2 - 4*y**2 - 4

def function2(x,y):
    return x+y-2

def poch_czastk(func,var=0,point=[]):
    args = point[:]

    def wraps(x):
        args[var] =x
        return func(*args)
    return derivative(wraps,point[var],dx=1e-6)

def Newton_Method(x,y,eps):

    i = 0
    Wk0= np.array([0,0])
    Wk1= np.array([x,y])
    while la.norm(Wk1-Wk0)>eps:
        Wk0=Wk1
        D= np.array( [ [poch_czastk(function1,0,[x,y]),poch_czastk(function1,1,[x,y])] , [poch_czastk(function2,0,[x,y]),poch_czastk(function2,1,[x,y])] ] )
        D_Inverse = np.linalg.inv(D)
        F = np.array([function1(x,y),function2(x,y)])
        Wk1 = Wk0 - D_Inverse.dot(F)
        x = Wk1[0]
        y = Wk1[1]
        i = i + 1
    return Wk1,i

print(Newton_Method(1,0,0.01))

x = numpy.linspace(-7,7,10000)
y = numpy.linspace(-7,7,10000)
y1 = x**2 - 4*y**2 - 4
y2 = x+y-2
plt.plot(x,y,y1)
plt.plot(x,y,y2)
plt.show()