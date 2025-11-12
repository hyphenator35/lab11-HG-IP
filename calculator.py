#https://github.com/hyphenator35/lab11-HG-IP
#Partner 1: Hunter Garcia
#Partner 2: Ian Pallapati

import math

def square_root(a):
  try:
    return math.sqrt(a)
  except ValueError:
    raise ValueError

def hypotenuse(a, b):
  try:
    return math.hypot(a, b)
  except ValueError:
    raise ValueError

def add(a, b):
  return a + b

def sub(a, b):
  return a - b
def subtract(a, b):
    return sub(a, b)

def mul(a, b):
  if a == 0:
    raise ZeroDivisionError
  else:
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
  if a <= 0 or b <= 0 or a == 1:
    raise ValueError
  return math.log(b, a)

def logarithm(a, b):
    return log(a, b)

def exp (a, b):
  return a**b
