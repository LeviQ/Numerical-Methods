import numpy as np

def LU_dolittle(A):

    n = len(A)
    L = [[0] * len(A[:][1]) for i in range(n)]
    U = [[0] * len(A[:][1]) for i in range(n)]

    for i in range(n):
        L[i][i] = 1
        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(0, i):
                U[i][j] = U[i][j] - L[i][k] * U[k][j]

        for j in range(i + 1, n):
            L[j][i] = A[j][i]
            for k in range(0, i):
                L[j][i] = (L[j][i] - L[j][k] * U[k][i]) / U[i][i]
    return U, L

macierz1 = ([[2, 5, 7], [6, 3, 4], [5,-2, -3]])
macierz2 = ([[1, 1], [1, 4]])
print(LU_dolittle(macierz1))
print("")
print(LU_dolittle(macierz2))