import csv
with open("text.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for dic in reader:
        print(dic)