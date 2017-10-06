import csv
nameFile=str(input("Enter the name of the file "))
with open(nameFile, "r", newline="") as file:
    reader = csv.DictReader(file)
    for dic in reader:
        print(dic)