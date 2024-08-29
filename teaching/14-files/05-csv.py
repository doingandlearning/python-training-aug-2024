import csv

with open("sample.csv", "w") as file:
  writer = csv.writer(file)
  writer.writerow(['She Loves You', 'Sept 1963'])
  writer.writerow(['I Want To Hold Your Hand', 'Dec 1963'])
  writer.writerow(['Can`t Buy Me Love', 'Apr 1964'])
  writer.writerow(['A Hard Days Night', 'Jul 1964'])