def print_my_msg(text, restart_time = "11.15"):
  print(text.replace("Coffee", "Water"))
  print(f"We will start back at {restart_time}.")


print_my_msg("Good morning! Coffee is at 11!")
print_my_msg("Good morning! Coffee is at 11!", "11.20")

def greeter(name, 
            title="Dr.", 
            prompt="Welcome", 
            message="Live long and prosper!"):
  print(f"{prompt} {title} {name} - {message}")

greeter("Kevin", title="Mr.", message="This is the way!")