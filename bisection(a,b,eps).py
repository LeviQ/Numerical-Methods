import math

def polynomial(f, x):
    l = len(f)
    result = 0
    for i in range(l):
        result += math.pow(x,i) * f[i]
    return result

def bisection(f, a, b, eps):
    if(polynomial(f, a) * polynomial(f, b) > 0):
        return "The interval that was entered is wrong!"

    d = 0
    meter = 0
    while((b-a)/math.pow(2, meter) > eps):
        d = (a + b) / 2.
        if(polynomial(f, d) == 0):
            return d
        if(polynomial(f, a) * polynomial(f, d) > 0):
            a = d
        if(polynomial(f, a) * polynomial(f, d) < 0):
            b = d
        meter = meter + 1
    return d


f1 = [2, 3, 1]
f2 = [5, 1]

eps = 0.000000000001

print(bisection(f1, -3.0, -1.0, eps))
print(bisection(f2, 12.0, -2.0, eps))
print(bisection(f2, -5.0, -1.0, eps))