import sys, csv
from tabulate import tabulate

table = []
if len(sys.argv) != 2:
    sys.exit("No of args not good")
name = sys.argv[1]

if name.endswith(".csv") == False:
    sys.exit("Not a csv file")
try:
    with open(name, "r") as file:
        title = next(csv.reader(file))
        for line in csv.reader(file):
            table.append(line)

except FileNotFoundError:
        sys.exit("File is not found")

#print(tabulate(table, tablefmt="grid"))
print(tabulate(table, title, tablefmt="grid"))
