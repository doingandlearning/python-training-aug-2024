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

  def __lt__(self, other):
    return self.amount < other.amount


q1 = Quantity(10, "London")
q2 = Quantity(5, "Glasgow")

print(q1 and q2)