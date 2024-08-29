def get_user_input():
  value = None
  try:
    value = float(input("Give me a value: "))
    if value == 0:
      raise ZeroDivisionError("Whoops! You were about to divide by zero - give me a new number")
  except ValueError as e:
    print("Couldn't convert input to float.")
    print(e)
    get_user_input()
  except ZeroDivisionError as e:
    print(e)
    get_user_input()
  except Exception as e:
    print("Something unexpected went wrong getting the user input")
    print(e)
    get_user_input()
  else:
    print("Everything went well - good luck!")
    print(f"That took a few times!")
    return value
  

  
user_input = get_user_input()

try:
  print(4/user_input)
except ZeroDivisionError:
  print("The user tried to divide by zero")

