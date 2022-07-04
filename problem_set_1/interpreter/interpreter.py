input = input("Insert your input")
x,y,z = input.split(' ', 2)
if y == "+":
    solution = float(int(x)+int(z))
elif y == "/":
    solution = float(int(x)/int(z))
elif y == "*":
    solution = float(int(x)*int(z))
elif y == "-":
    solution = float(int(x)-int(z))
else:
    print("wrong parameteres")

print(solution)