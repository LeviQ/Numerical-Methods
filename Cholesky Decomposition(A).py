import numpy as np

def cholesky_decomposition(A):

    n = len(A)
    L = [[0] * len(A[:][1]) for i in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i == j:
                L[i][i] = A[i][i]
                for k in range(0, i):
                    L[i][i] = L[i][i] - pow(L[i][k], 2)
                L[i][i] = np.sqrt(L[i][i])
            else:
                L[j][i] = A[j][i]
                for k in range(0, i):
                    L[j][i] = L[j][i] - L[j][k] * L[i][k]
                L[j][i] = L[j][i] / L[i][i]
    return L

print(cholesky_decomposition([[4, -6, 8], [-6, 10, -10], [8, -10, 29]]))
print("")
print(cholesky_decomposition([[1, -1, 2], [-1, 5, -4], [2, -4, 6]]))
