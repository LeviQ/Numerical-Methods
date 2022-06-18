import numpy as np

### Matrix multiplication in a loop
def Matrix_Multiplication(A, B):
    c = [[0] * len(B[0]) for i in range(len(A))] ### Initialization of the zero matrix, getting column number from B and line number form A.
    for i in range(len(A)):          
        for j in range(len(B[0])):
            for k in range(len(B)):
                c[i][j] = c[i][j] + A[i][k] * B[k][j]
    print(c)

Matrix_Multiplication([[2, 3], [4, 5]], [[5, 1], [2, 3]])
Matrix_Multiplication([[1, 4, 7], [2, 5, 8]], [[1, 4], [2, 5], [3, 6]])
Matrix_Multiplication([[1, 4, 5, 2], [2, 10, 5, 2]], [[5, 4], [2, 3], [5, 5], [3, 3]])
Matrix_Multiplication([[5, 1, 5], [10, 2, 6], [4, 3, 1]], [[10, 2, 1, 4], [6, 2, 3, 3], [2, 2, 2, 2]])
