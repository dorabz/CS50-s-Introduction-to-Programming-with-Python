import inflect
p = inflect.engine()
import sys

list = []
while True:
    try:
        name = input("Name:")
        if len(name) == 0:
            sys.exit()
        list.append(name)
    except EOFError:
            print("Adieu, adieu, to " + p.join(list))
            break
    else:
            continue
