# num = int(input("Enter a number to check for: "))

for i in range(0, 10):
  print(i, end=" ")
  if i % 2 == 1:
    continue
  print("We love even numbers!")
     

print("Done")