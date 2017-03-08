from math import *

h = 1/10000000

derivate = lambda f, x = 0: (f(x + h) - f(x))/h

func = lambda x: x ** 3

print(derivate(func, 2))