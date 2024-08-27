my_variable = 'Gary'
print(my_variable)
my_variable = "Gary's been working at the BBC for two year."
print(my_variable)
my_variable = 'Gary says that "Red teaming sounds fun."\n Gary\'s right!'
print(my_variable)
my_variable = """
Hello
  World!
"""
print(my_variable) # 16


print(len(my_variable))
string_1 = "good"
string_2 = "morning"
print(string_1 + string_2)
# print(string_1 + 3) . - Can't do this!

msg = "Hello World, World, World, World"
print(msg.replace("World", "BBC"))
print(msg)
print(msg.find("World"))
print(msg.find("breakfast"))
print(1 == "1")
print("1")
print("Kevin".startswith("C")) # Bool -> True/False
print("123THIS❌".isalnum())

location = "Belfast"
name = "Kevin"
pet = "Star"

print("My name is" + name + ", I am in " + location + ". My pet is called"  + pet + ".")
print(f"My name is {name}, I am in {location}. My pet is called {pet}, he is {1 + 8} months old .")
