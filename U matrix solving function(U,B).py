import numpy as np

### Solving the system of equations with the upper triangular matrix
def U_matrix_solving_function(U,b):      ### U is the upper matrix, b - vector of intercepts
    A = [0] * len(U[0]) ### Our matrix initially filled with zeros
    for i in range(len(U)):
        c = len(U) - i - 1
        A[c] = b[c]     
        for j in range(i+1):
            d = len(U[c]) - 1 - j
            if c == d: continue
            A[c] = A[c] - U[c][d] * A[d]    
        A[c] = A[c] / U[c][c]               
    return A

print(U_matrix_solving_function([[3, -4, 3], [0, 2, 3], [0, 0, -2]], [23, 2, -4]))
print(U_matrix_solving_function([[4, 5, 2], [0, 5, 1], [0, 0, -6]], [15, 5, 12]))
