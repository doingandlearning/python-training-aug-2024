# while <test>:
#   __code_to_run__

valid_data = False

while not valid_data:
  age = int(input("Please enter your age:"))
  if age < 0 or age > 120:
    print("invalid age")
  else:
    valid_data = True

print(f"The age is {age}.")
print("All done.")