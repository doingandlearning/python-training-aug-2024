count = 0

def my_func():
  # count = 10 # shadow
  global count
  count += 10
  name = "Kevin"
  print(count)
  print(name)


print(count)
my_func()
print(count)
