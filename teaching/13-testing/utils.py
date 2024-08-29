def add(a, b):
  # a and b are either float or ints
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise ValueError("Parameters must be numbers")
  return a + b