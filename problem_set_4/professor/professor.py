import random

def main():
    l = get_level()
    i = 0
    score = 0
    while i < 10:
        a, b = generate_integer(l)
        flag = 0
        j = 0
        while j < 3:
            try:
                ab = int(input(f"{a} + {b} = "))
                if ab == (a + b):
                    flag = 1
                    break
                else:
                    print("EEE")
                    j += 1
            except:
                print("EEE")
                j += 1
                pass
        print(f"{a} + {b} = {a + b}")
        i += 1
        if flag == 1:
            score += 1
    print(" ", score)


def get_level():
    while True:
        try:
            l = int(input("Level:"))
            if l==1 or l==2 or l==3:
                break
        except ValueError:
            continue
    return l

def generate_integer(level):
    if level == 1:
        a = random.randint(0,9)
        b = random.randint(0,9)
    elif level == 2:
        a = random.randint(10,99)
        b = random.randint(10,99)
    elif level == 3:
        a = random.randint(100,999)
        b = random.randint(100,999)
    return a,b

if __name__ == "__main__":
    main()