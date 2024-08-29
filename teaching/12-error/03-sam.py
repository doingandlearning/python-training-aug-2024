try: 
  result = Process(-3, 4)
  print(f"Processing succeeded: {result}")
except Exception as e:
  if isinstance(e, ZeroDivisionError):
    pass
  elif isinstance(e, ValueError):
    pass
 