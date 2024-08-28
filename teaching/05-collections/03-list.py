my_list = []
print(my_list)
print(type(my_list))

list1 = ["John", "Paul", "George", "Ringo"]
print(len(list1))
print(list1[::-1]) # All the slicing is the same 

list1.append("Kevin")
print(list1)

list1.extend(["Rina", "Gary"])
print(list1)

list1.insert(2, "Sam")
print(list1)

list1.remove("John")
print(list1)

del list1[1:3]
print(list1)

list2 = list1.copy()
list2.append("George")
print(list1)

me = list1.pop(2)
print(list1)
print(me)