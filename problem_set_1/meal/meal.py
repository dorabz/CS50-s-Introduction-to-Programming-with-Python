def main():
    time = input("What's the time?")
    time_2 = convert(time)
    if 7 <= time_2 <= 8:
        print("breakfast time")
    if 12 <= time_2 <= 13:
        print("lunch time")
    if 18 <= time_2 <= 19:
        print("dinner time")

def convert(time):
     hours, minutes = time.split(":")
     return float(hours)+float(minutes)/60


if __name__ == "__main__":
    main()