def square(n):
  return n * n
  ### TEMPORAL DEAD ZONE ###
  n ** 2
  

result1 = square(7)
result2 = square(11)

print(result1)
print(result2)

if square(3) < 15:
  print(f"Still less than 15. {square(4)} is bigger than 15.")

# first class!