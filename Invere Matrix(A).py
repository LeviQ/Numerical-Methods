import numpy as np

def Inverse_Matrix(A): ### A - matrix of coefficients of the system of equations

    n = len(A)

    L = np.identity(n)

    for i in range(n - 1):
        for j in range(i + 1, n):
            m = A[j][i] / A[i][i]               ### Gauss-Jordan Calculating
            for k in range(i, n):
                A[j][k] = A[j][k] - m * A[i][k]
                L[j][k] = L[j][k] - m * L[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i-1, -1, -1):
            m = A[j][i]/A[i][i]                 ### Calculation of coefficients
            for k in range(i, 0, -1):           ### We do not delete the last line
                A[j][k] = A[j][k] - m * A[i][k]
            for k in range(n-1, -1, -1):
                L[j][k] = L[j][k] - m * L[i][k]

    for i in range(n):
        tmp = A[i][i]
        A[i][i] = A[i][i]/A[i][i]               ### Result
        for j in range(n):
            L[i][j] = L[i][j]/tmp
    return L

matrix1 = ([[2, 5, 7], [6, 3, 4], [5,-2, -3]])
matrix2 = ([[1, 1], [1, 4]])
print(Inverse_Matrix(matrix1))
print("")
print(Inverse_Matrix(matrix2))