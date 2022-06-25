import numpy as np
import math

def Gauss_Pivot(A, b): ### A - matrix of coefficients of the system of equations, b - vector of intercepts

    n = len(A)

    for i in range(n-1):
        l = i
        for j in range(i+1, n):
            if np.abs(A[l][i]) < np.abs(A[j][i]):
                l = j
        A[[i, l]] = A[[l, i]]
        b[[i, l]] = b[[l, i]]
        for j in range(i+1, n):
            m = A[j][i] / A[i][i]
            b[j] = b[j] - m * b[i]
            for k in range(i, n):
                A[j][k] = A[j][k] - m * A[i][k]

    x = [[0] for i in range(len(b))]

    x[len(b) - 1] = b[len(b) - 1] / A[len(b) - 1][len(b) - 1]

    for j in range(len(b) - 2, -1, -1):
        z = 0;
        for k in range(len(b) - 1, j, -1):
            z += A[j][k] * x[k]
        x[j] = (b[j] - z) / A[j][j]
    return x


matrix1 = np.array([[2., 1., 4.], [6., 6., 14.], [4., 14., 19.]])
vector1 = np.array([[1.], [8.], [25.]])
matrix2 = np.array([[2., -3., -1.], [-4., 10., 5.], [8., -4., 4.]])
vector2 = np.array([[9.], [-29.], [12.]])
print(Gauss_Pivot(matrix1,vector1))
print(Gauss_Pivot(matrix2,vector2))