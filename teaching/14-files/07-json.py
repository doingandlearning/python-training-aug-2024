# JSON - JavaScript Object Notation
import json

things_we_have_learned = {
  "Functions": ["Default parameters", "Arbitrary parameters"],
  "Classes": ["__init__", "__add__"],

}

with open("../store.json", "w") as file:
  file.write(json.dumps(things_we_have_learned))

