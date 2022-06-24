import numpy as np

###Solving a system of equations with a lower triangular matrix
def L_Matrix_solving_function(L, b):     ### L is the bottom matrix, b - vector of intercepts
    A = [0] * len(L) 
    for i in range(len(L)): ### Rows of the lower triangular matrix
        A[i] = b[i]
        for j in range(len(L[i])):  ### Columns of the lower triangular matrix
            if i == j: continue
            A[i] = A[i] - L[i][j] * A[j] 
        A[i] = A[i] / L[i][i]
    return A

print(L_Matrix_solving_function([[-2, 0, 0], [1, 3, 0], [4, 2, 2]], [2, 5, 2]))
print(L_Matrix_solving_function([[4, 0, 0], [4, 3, 0], [9, 8, 1]], [5, 10, 2]))
