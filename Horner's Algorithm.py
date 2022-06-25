import numpy as np

def Heron(a, c):     ### a is an array of coefficients, c - value in binomial: (x - c)

    l = len(a)   ### We initialize the variable l as the length of the array A
    b = [[0] for i in range(len(a))]
    b[0] = a[0]  ### We rewrite the first factor unchanged into our table
    for i in range(1, l):
        b[i] =  c * b[i - 1] + a[i]     
    print("Successive Factors, where the last one is the Remainder")
    for i in range(len(b)):    ### Getting results
        print(b[i])
Heron([2,-5,4,-1],1)
Heron([2,-5,4,4,0,2],2)    
Heron([4,2,1,-5,2,1,3,-2],1)
