import numpy as np

### We're adding matrices in a loop
def Matrix_Addition(A, B):
    c = [[0] * len(A[0]) for i in range(len(A))]  ### Initialization of the zero matrix
    for i in range(len(A)):                       ### i = line number
        for j in range(len(A[0])):                ### j = column number
            c[i][j] = A[i][j] + B[i][j]           ### Filling our matrix with results
    print(c)

Matrix_Addition([[2, 3], [4, 5]], [[5, 1], [2, 3]])
Matrix_Addition([[2, 3, 1], [1, 3, 1], [5, 12, 1]], [[2, 3, 2], [1, 3, 5], [2, 1, 11]])
Matrix_Addition([[2, 3], [1, 3], [5, 12]], [[2, 3], [1, 3], [2, 1]])
Matrix_Addition([[2, 3, 1, 2], [1, 3, 1, 5], [5, 12, 5, 1]], [[2, 3, 8, 1], [1, 3, 4, 6], [2, 1, 9, 10]])

### Console Results:
### [[7, 4], [6, 8]]
### [[4, 6, 3], [2, 6, 6], [7, 13, 12]]
### [[4, 6], [2, 6], [7, 13]]
### [[4, 6, 9, 3], [2, 6, 5, 11], [7, 13, 14, 11]]