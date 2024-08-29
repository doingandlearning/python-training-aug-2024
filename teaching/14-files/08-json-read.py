import json

data = None

with open("store.json") as file:
  data = json.load(file)

print(data["Functions"])