try:
  with open("test.txt") as file:
    lines = file.readlines()
    for line in lines:
      print(line)
except FileNotFoundError:
  print("Whoops! That file doesn't exist!")

# auto closed !!