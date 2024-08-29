import traceback

try:
  4/0
except Exception as e:
  print("Whoops!")
  traceback.print_exc()

