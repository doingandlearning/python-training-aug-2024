# def function_name(para1, para2, para3):
#   """
#   This function is used for.
#   """
#   statements
#   pass


# Don't Repeat Yourself

def print_msg():
  print("Hello world!")

print_msg()

def print_my_msg(text, restart_time):
  print(text.replace("Coffee", "Water"))
  print(f"We will start back at {restart_time}.")

print_my_msg("Good morning! Coffee is at 11!", "11.15")
# positional arguments