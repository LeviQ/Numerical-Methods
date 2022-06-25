import numpy as np

def Gauss_Jordan(A,b):  ### matrix of coefficients of the system of equations, b - vector free words

    n = len(A)

    for i in range(n - 1):
        for j in range(i + 1, n):
            m = A[j][i] / A[i][i]             ### Gaussian enumeration
            b[j] = b[j] - m * b[i]
            for k in range(i, n):
                A[j][k] = A[j][k] - m * A[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            m = A[j][i]/A[i][i]
            b[j] = b[j] - m * b[i]
            for k in range(i, 0, -1):
                A[j][k] = A[j][k] - m * A[i][k]

    for i in range(n):
        b[i] = b[i]/A[i][i]
        A[i][i] = A[i][i]/A[i][i]
    return A, b


print(Gauss_Jordan([[2, 1, 4], [6, 6, 14], [4, 14, 19]], [1, 8, 25]))
print(Gauss_Jordan([[2, -3, -1], [-4, 10, 5], [8, -4, 4]], [9, -29, 12]))