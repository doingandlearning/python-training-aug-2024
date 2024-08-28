def sum2(a, b):
  return a + b

def sum3(a,b,c):
  return a + b + c

def sum(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total 

print(sum(1,2))
print(sum(1,14,54))
print(sum(76,93, 11))

def greet(message, *names):
  for name in names:
    print(f"{message} {name}!")

greet("Are you still awake,", "Scott", "Mustafa", "Rina", "Gary", "Natalie", "Adhiraj")
greet("Are you listening,", "Scott", "Mustafa", "Rina", "Gary", "Natalie", "Adhiraj")

