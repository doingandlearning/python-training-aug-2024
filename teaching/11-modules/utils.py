"""
This is a sample utility library.
"""
PI = 3.14159

class Shape:
  def __init__(self, id):
    self.id = id

  def __str__(self):
    return f"Shape:{self.id}"

default_shape = Shape("square")

def printer(object):
  print("I am a great printer")
  print(object)
  print("--------------------")

def main():
  printer(default_shape)
  print(__name__)


if __name__ == "__main__":
  main()