class Quantity:
  def __init__(self, amount: int, location: str): 
    self.amount = amount
    self.location = location
  
  def __add__(self, other):
    if self.location != other.location:
      return self
    return Quantity(self.amount + other.amount, self.location)

  def __sub__(self, other):
    if self.location != other.location:
      return self
    return Quantity(self.amount - other.amount, self.location)    

  def __mul__(self, other):
    if isinstance(other, int):
      return Quantity(self.amount * other, self.location)
    return Quantity(self.amount * other.amount, self.location)

  def __repr__(self):
    return f"Quantity({self.amount}, {self.location})"

q1 = Quantity(5, "London")
q2 = Quantity(10, "London")
q3 = q1 + q2  # Quantity(15)
q4 = q3 - q1
q5 = q1 - q2
q6 = q1 * 5
# q1.add(q2) => Quantity(15)
# q1 + q2 = Quantity(15)

# +
print(q1)
print(q2)
print(q3)
print(q4)
print(q5)
print(q6)