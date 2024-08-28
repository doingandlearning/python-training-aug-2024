class Person:
  """
  An example class to hold details about a person
  """
  def __init__(self, name: str, age: int, rate_of_pay: float = 11.44):    # dunder init => __init__
    self.name = name
    self.age = age # filter, edit, do some kind of check!
    self.rate_of_pay = rate_of_pay

  def __repr__(self):
    return f"Person('{self.name}', {self.age})"

  def copy(self):
    return Person(self.name, self.age)

  def birthday(self):
    print(f"Happy birthday you were {self.age}")
    self.age += 1
    print(f"You are now {self.age}")
  
  def is_teenager(self):
    return self.age < 20 and self.age > 12
  
  def calculate_pay(self, hours_worked):
    return hours_worked * self.rate_of_pay


# encapsulated

kevin = Person("Kevin", 41) # initialises -> __init__
ridwan = Person("Ridwan", 23) 

not_kevin = kevin.copy()
not_kevin.name = "Rina"
not_kevin.age = 24

print(id(not_kevin))
print(id(kevin))


kevin.birthday()
ridwan.birthday()
not_kevin.birthday()

print(kevin.is_teenager())
ethan = Person("Ethan", 13)

print(ethan.is_teenager())
print(kevin.calculate_pay(8))

del kevin
print(kevin)