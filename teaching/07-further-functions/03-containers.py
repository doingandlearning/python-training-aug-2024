num_list = [1,3, 5,7,2,7,4,10]

# Higher Order Functions -> function that takes a function

def is_even(num):
  return num % 2 == 0

num_list = [1,3, 5,7,2,7,4,10]
print(list(filter(is_even, num_list)))
print(list(filter(lambda num: num % 2 == 0, num_list)))
print(filter(lambda num: num % 2 == 0, num_list))

def double(num):
  return num * 2

num_list = [1,3, 5,7,2,7,4,10]
print(list(map(double, num_list)))
print(list(map(lambda num: num*2, num_list))) # Readable

print(list(map(double, filter(is_even, num_list))))

def kevin_high_order(func1, data):
  return func1(data)

print(kevin_high_order(tuple, "Hello"))