# lambda arguments: expression

func0 = lambda: print("I have no arguments.")
func0()

def func0():
  print("I have no arguments.")
func0()

square = lambda x: x * x # implicit return
print(square(4))

def square(x):
  return x * x
print(square(4))

product = lambda x,y: x * y
print(product(4,5))

def product(x, y):
  return x * y
print(product(4,5))

