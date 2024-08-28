empty_tuple = ()
print(type(empty_tuple))
# .     0 1 2 3
tup1 = (1,3,5,7)
print(tup1[0])
print(tup1[1])
print(tup1[1:3]) # [start (inclusive): end (exclusive)]
print(tup1[1:])
print(tup1[:2]) # slice of tuple
print(tup1[0:3:2])
print(tup1[::2])
print(tup1[::-1])

tup2 = (2, False, "Kevin", -23.45)

for value in tup2:
  print(value)

if 1 in tup2:
  print("It was there!")

tup3 = ('apple', 'pear', 'orange', 'plum', 'apple')

for fruit in tup3:
  print(fruit)


