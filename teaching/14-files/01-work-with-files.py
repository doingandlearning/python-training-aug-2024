file_handle = open("test.txt") # handle

print(file_handle) # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

# .readline() => line by line
# .readlines() => iterable of all the lines
lines_of_file = file_handle.readlines()

for line in lines_of_file:
  print(line)

file_handle.close()