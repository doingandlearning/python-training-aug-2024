age = 18
status = None

if age < 18:
  status = "child"
else:
  status = "adult"

print(status)

status = "child" if age < 18 else "adult"

# <true-result> if <condition> else <false-result>

print(status)