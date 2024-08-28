empty_dictionary = {}
print(type(empty_dictionary))

cities = {
  "England": "London",
  "Scotland": "Edinburgh",
  "NI": "Belfast",
  "Wales": "Cardiff"
}
print(cities)

print(cities["England"])
print(cities.get("Wales"))

for country in cities:
  print(f"The capital of {country} is {cities[country]}")

print(cities.values())
print(cities.keys())
print(cities.items())

print('Wales' in cities)
print('Cardiff' in cities)

cities.setdefault("France", "Paris")
print(cities)

cities.setdefault("France", "Berlin")
print(cities)