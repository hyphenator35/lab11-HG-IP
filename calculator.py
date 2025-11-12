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
