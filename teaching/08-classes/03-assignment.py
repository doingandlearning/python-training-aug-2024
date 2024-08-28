class Person:
  def __init__(self, name, age):    # dunder init => __init__
    self.name = name
    self.age = age # filter, edit, do some kind of check!

  def __repr__(self):
    return f"Person('{self.name}', {self.age})"


# encapsulated

kevin = Person("Kevin", 41) # initialises -> __init__
ridwan = Person("Ridwan", 23) 

not_kevin = kevin
not_kevin.name = "Rina"
not_kevin.age = 24

print(id(not_kevin))
print(id(kevin))