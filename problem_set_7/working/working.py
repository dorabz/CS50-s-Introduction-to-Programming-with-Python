import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        time_parse = re.search(r"^((1[0-2]|0?[1-9]):*([0-5][0-9])*) ?([AP][M]) to ((1[0-2]|0?[1-9]):*([0-5][0-9])*) ?([AP][M])$", s)
        groups = time_parse.groups()
       # print(groups[1], groups[2], groups[3])
        # print(groups[5], groups[6], groups[7])
        if int(groups[1]) <= 12 and int(groups[5]) <= 12:
            h1 = int(groups[1])
            h2 = int(groups[5])
            m1 = groups[2]
            m2 = groups[6]
            flag1 = groups[3]
            flag2 = groups[7]
            if flag1 == 'AM':
                if h1 == 12:
                    nh1 = 0
                if h1 != 12:
                    nh1 = h1
            if flag2 == 'AM':
                if h2 == 12:
                    nh2 = 0
                if h2 != 12:
                    nh2 = h2
            if flag1 == 'PM':
                if h1 == 12:
                    nh1 = 12
                else:
                    nh1 = h1 + 12
            if flag2 == 'PM':
                if h2 == 12:
                    nh2 = 12
                else:
                    nh2 = h2 + 12
            if m1 == None:
                t1 = f"{nh1:02}:00"
            if m1 != None:
                t1 = f"{nh1:02}:{m1}"
            if m2 == None:
                t2 = f"{nh2:02}:00"
            if m2 != None:
                t2 = f"{nh2:02}:{m2}"
            return f"{t1} to {t2}"
    except Exception:
        raise ValueError



if __name__ == "__main__":
    main()