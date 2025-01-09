import math

def f_sum(a,b):
   return a+b
def f_d(a,b):
   return a-b
def f_p(a,b):
   return a*b*2

def squareTriangle(a, b, c):

   p = (a + b + c) / 2

   return math.sqrt(p * (p - a) * (p - b) * (p - c))