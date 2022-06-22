import numpy as np

### Algorytm eliminacjii Gaussa bez wyboru elementu czesciowego, ale ze znajdowaniem rozkładu LU
def Lewicki_Aleksander_gauss(A, b): ### A - macierz wspołczynników układu rownań, b - wektor wyrazow wolnych
    L = len(A) * [0]
    for i in range(len(A)):
        L[i] = len(A[i]) * [0]
                                     ### Tworzymy macierze dolnotrojkątne i gornotrojkątne
    U = len(A) * [0]
    for i in range(len(A)):
        U[i] = len(A[i]) * [0]

    for i in range(len(L)):          ### W miejsca Diagonali wstawiamy 1
        L[i][i] = 1

    for j in range(len(A[0])):       ### kolumny
        for i in range(len(A)):      ### wiersze
            if i > j:
                L[i][j] = A[i][j]
                for k in range(j):
                    L[i][j] -= L[i][k] * U[k][j]
                L[i][j] /= U[j][j]
            if i <= j:
                U[i][j] = A[i][j]
                for k in range(i):
                    U[i][j] -= L[i][k] * U[k][j]

    Y = len(L) * [0]                ### Układ rownan: Ly = b
    for i in range(len(L)):
        Y[i] = b[i]
        for j in range(len(L[i])):
            if i == j: continue
            Y[i] -= L[i][j] * Y[j]
        Y[i] /= L[i][i]


    X = [0] * len(U[0])             ### Układ rownan Ux = y
    for i in range(len(U)):
        m = len(U) - i - 1
        X[m] = Y[m]
        for j in range(i + 1):
            n = len(U[m]) - 1 - j
            if m == n: continue
            X[m] -= U[m][n] * X[n]
        X[m] /= U[m][m]
    return X


### Wykonujemy testy naszego Gaussa
print(Lewicki_Aleksander_gauss([[2, -3, -1], [-4, 10, 5], [8, -4, 4]], [9, - 29, 12]))
print(Lewicki_Aleksander_gauss([[-2, 0, 0], [1, 3, 0], [4, 2, 2]], [2, 5, 2]))