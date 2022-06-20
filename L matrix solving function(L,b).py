import numpy as np

### Rozwiazywanie układu rownań z macierza dolna trojkatna
def Lewicki_Aleksander_ukladL(L, b):     ### L to macierz dolna, b - wektor wyrazów wolnych
    A = [0] * len(L) ### Tworzymy pustą macierz
    for i in range(len(L)): ### Wiersze macierzy trojkątnej dolnej
        A[i] = b[i]
        for j in range(len(L[i])):  ### Kolumny macierzy trojkątnej dolnej
            if i == j: continue
            A[i] = A[i] - L[i][j] * A[j]      ### Obliczenia
        A[i] = A[i] / L[i][i]
    return A
### Testy rozwiązania macierzy:
print(Lewicki_Aleksander_ukladL([[-2, 0, 0], [1, 3, 0], [4, 2, 2]], [2, 5, 2]))
print(Lewicki_Aleksander_ukladL([[4, 0, 0], [4, 3, 0], [9, 8, 1]], [5, 10, 2]))