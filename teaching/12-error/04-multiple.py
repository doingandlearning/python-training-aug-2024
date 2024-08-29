try:
  # This will be caught the outer most except
  try:
    try:
      raise ValueError("Whoops! Something went wrong!")
    except Exception as e:
      raise e
  except Exception as e:
    print("level 2")
    print(e)
    
except:
  print("Something went wrong with the program") 

