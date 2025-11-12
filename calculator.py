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

def mul(a, b):
  if a == 0:
    raise ZeroDivisionError
  else:
    return a * b

def div(a, b):
  return b / a

def log(a, b):
  if a <= 1 or b < 1:
    raise ValueError
  else:
    return math.log(b, a)

def exp(a, b):
  return math.exp(a, b)
