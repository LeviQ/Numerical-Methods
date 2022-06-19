import numpy as np

### Algorytm Hornera dzielenia wielomianu przez dwumian
def Lewicki_Aleksander_heron(a, c):     ### a to tablica wspołczynników, c - wartosc w dwumianie: (x - c)

    l = len(a)   ### Inicjujemy zmienną l jako długość tablicy A
    b = [[0] for i in range(len(a))]
    b[0] = a[0]  ### Pierwszy wspołczynnik przepisujemy bez zmian do naszej tablicy
    for i in range(1, l):
        b[i] =  c * b[i - 1] + a[i]     ### Wyliczanie wyników i uzupełnianie nimi naszą tablicę
    print("Kolejne Współczynniki, gdzie ostatni z nich to Reszta")
    for i in range(len(b)):    ### Wypisywanie wyników z tablicy
        print(b[i])
Lewicki_Aleksander_heron([2,-5,4,-1],1)
Lewicki_Aleksander_heron([2,-5,4,4,0,2],2)    ### Kiedy nie ma współczynnika przy danej potędze, w tym wypadku przy x, to wpisujemy 0
Lewicki_Aleksander_heron([4,2,1,-5,2,1,3,-2],1)
