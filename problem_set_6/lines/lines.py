import sys

if len(sys.argv) != 2:
    sys.exit("No  of args not good")
name = sys.argv[1]
lines = 0
hashtag=0
space=0
if name.endswith(".py") == False:
    sys.exit("Not a python file")
try:
    with open(name, "r") as file:
        for line in file:
            if line.lstrip().startswith('#'):
                hashtag+=1
            elif line.isspace():
                space+=1
            else:
                lines+=1
except FileNotFoundError:
        sys.exit("File is not found")

print(lines)
