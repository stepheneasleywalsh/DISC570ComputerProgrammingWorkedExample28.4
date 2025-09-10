import math

def f(x):
   if type(x) == int:
       return math.factorial(x)
   elif type(x) == float:
       raise TypeError("I can't calculate that")

x = 5.0
print(f(x))