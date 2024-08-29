import csv

with open("sample.csv") as file:
  reader = csv.reader(file)
  for row in reader:
    print(f"Title: {row[0]} and release date: {row[1]}")