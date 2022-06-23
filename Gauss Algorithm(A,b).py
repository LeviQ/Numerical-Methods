import numpy as np


def Gauss_Algorithm(A, b): ### A -matrix of coefficients of the system of equations, b - vector free words
    L = len(A) * [0]
    for i in range(len(A)):
        L[i] = len(A[i]) * [0]
                                     
    U = len(A) * [0]
    for i in range(len(A)):
        U[i] = len(A[i]) * [0]

    for i in range(len(L)):          
        L[i][i] = 1

    for j in range(len(A[0])):       ### columns
        for i in range(len(A)):      ### rows
            if i > j:
                L[i][j] = A[i][j]
                for k in range(j):
                    L[i][j] -= L[i][k] * U[k][j]
                L[i][j] /= U[j][j]
            if i <= j:
                U[i][j] = A[i][j]
                for k in range(i):
                    U[i][j] -= L[i][k] * U[k][j]

    Y = len(L) * [0]                ### Ly = b
    for i in range(len(L)):
        Y[i] = b[i]
        for j in range(len(L[i])):
            if i == j: continue
            Y[i] -= L[i][j] * Y[j]
        Y[i] /= L[i][i]


    X = [0] * len(U[0])             ### Ux = y
    for i in range(len(U)):
        m = len(U) - i - 1
        X[m] = Y[m]
        for j in range(i + 1):
            n = len(U[m]) - 1 - j
            if m == n: continue
            X[m] -= U[m][n] * X[n]
        X[m] /= U[m][m]
    return X


### Testing Gauss
print(Gauss_Algorithm([[2, -3, -1], [-4, 10, 5], [8, -4, 4]], [9, - 29, 12]))
print(Gauss_Algorithm([[-2, 0, 0], [1, 3, 0], [4, 2, 2]], [2, 5, 2]))
