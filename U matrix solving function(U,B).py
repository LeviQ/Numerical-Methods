import numpy as np

### Rozwiazywanie układu rownan z macierza gorną trojkątną
def Lewicki_Aleksander_ukladU(U,b):      ### U to macierz gorna, b - wektor wyrazow wolnych
    A = [0] * len(U[0]) ### Nasza macierz poczatkowo wypełniona zerami
    for i in range(len(U)):
        c = len(U) - i - 1
        A[c] = b[c]     ### Uzupełnianie naszej macierzy
        for j in range(i+1):
            d = len(U[c]) - 1 - j
            if c == d: continue
            A[c] = A[c] - U[c][d] * A[d]    ### Wyliczanie poszczegolnych x
        A[c] = A[c] / U[c][c]               ### ^^
    return A
### Testy rozwiązania macierzy:
print(Lewicki_Aleksander_ukladU([[3, -4, 3], [0, 2, 3], [0, 0, -2]], [23, 2, -4]))
print(Lewicki_Aleksander_ukladU([[4, 5, 2], [0, 5, 1], [0, 0, -6]], [15, 5, 12]))