import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    if n > 0:
        break
x = random.randint(1, n)

while True:
    try:
        p = int(input("Guess:"))
    except ValueError:
        continue
    else:
        if p < x:
            print("Too small!")
        elif p > x:
            print("Too large!")
        elif p == x:
            print("Just right!")
            break