import numpy as np
import matplotlib.pyplot as plt
import math

def Wiel(f, x):
    l = len(f)
    result = 0
    for i in range(l):
        result += f[i] * x**i
    return result


def incisal(f, x1, x2, eps):
    num = 200
    x_k = x1
    x_k1 = x2
    arg = np.array([x_k, x_k1])

    while (abs(x_k1 - x_k) > eps):
        x_k1n = x_k1 - (((x_k1 - x_k) * Wiel(f, x_k1)) / (Wiel(f, x_k1) - Wiel(f, x_k)))
        x_k = x_k1
        x_k1 = x_k1n
        arg = np.append(arg, x_k1n)

    value = Wiel(f, arg)
    main_args = np.linspace(x1-1, x2+1, num)
    main_f = Wiel(f, main_args)
    n = len(arg)
    x_0 = arg[n-1]
    y_0 = Wiel(f, x_0)
    print(x_0)
    print(y_0)

    plt.title("Incisal Method", fontsize=11, )
    plt.xlabel("Ox")
    plt.ylabel("Oy")

    plt.plot(main_args, main_f, color = "red", linewidth = 1.5)
    plt.plot(arg, value, linewidth=1, color="navy")
    plt.scatter(x_0, y_0, color="black", linewidth=2)

    plt.show()

f = [1, 0, 2, -5]

x1 = 2
x2 = 3
eps = 0.000000001

incisal(f, x1, x2, eps)