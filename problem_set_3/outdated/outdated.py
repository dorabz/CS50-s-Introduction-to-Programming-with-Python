
dict = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" :11,
    "December" : 12,
}

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            m, d, y = date.split("/")
            y = y.replace(" ", "")
            if int(d)<=31 and int(m)<=12:
                print(f"{y}-{int(m):02}-{int(d):02}")
                break
        elif "," in date:
            date2 = date.replace(" ", "*")
            m, d, y = date2.split("*")
            d = d.replace(",", "")
            if m in dict and int(d)<=31:
                print(f"{y}-{int(dict.get(m)):02}-{int(d):02}")
                break
    except ValueError:
        pass


