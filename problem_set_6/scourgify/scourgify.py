import sys, csv

if len(sys.argv) != 3:
    sys.exit("No of args not good")
name = sys.argv[1]
new = sys.argv[2]
table = []

if name.endswith(".csv") == False:
    sys.exit("Not a csv file")
try:
    with open(name, "r") as file:
        for line in csv.DictReader(file):
            surname, name = line['name'].split(",")
            name = name.lstrip()
            surname = surname.lstrip()
            house = line['house']
            table.append({"first": name, "last": surname, "house": house})

except FileNotFoundError:
        sys.exit("File is not found")

with open(new, "w") as file:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for line in table:
        writer.writerow({"first": line['first'], "last": line['last'], "house": line['house']})



