import math

import math
# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
       raise ZeroDivisionError("Can't be dividing by zero.")
    else:
     return b / a
def log(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)
def exp (a, b):
    return a**b
def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  if a == 0:
    raise ZeroDivisionError
  else:
    return a * b

def log(a, b):
  if a <= 1 or b < 1:
    raise ValueError
  else:
    return math.log(b, a)

def exp(a, b):
  return math.exp(a, b)
