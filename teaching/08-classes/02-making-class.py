class Person:
  def __init__(self, name, age):    # dunder init => __init__
    self.name = name
    self.age = age # filter, edit, do some kind of check!

  def __repr__(self):
    return f"Person('{self.name}', {self.age})"


# encapsulated

kevin = Person("Kevin", 41) # initialises -> __init__
ridwan = Person("Ridwan", 23) 
print(type(kevin)) # <class '__main__.Person'>
print(kevin.age)
print(kevin.name)
print(ridwan.name)
print(ridwan.age)

print(id(kevin))
print(id(ridwan))

print(kevin) # Person("Kevin", 41)
print(ridwan) # "Person with name Ridwan and age 23"

print(dir(kevin))
print(kevin.__repr__())

# class MathFunctions:
#   def add(a,b):
#     return a + b

# print(MathFunctions.add(1,2))