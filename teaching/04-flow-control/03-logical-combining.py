age = 102
status = None

if age > 12 and age < 20: # &&
  status = "teenager"
elif age < 18 or age > 68:
  status = "economically non-productive"
else:
  status = "not teenager"

print(status)

if not age < 100:
  print("Do you get a letter from the king?")