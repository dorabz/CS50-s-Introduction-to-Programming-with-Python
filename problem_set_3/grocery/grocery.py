dict = {}

while True:
    try:
        item = input("")
        if item.upper() in dict:
            dict[item.upper()] = int(dict.get(item.upper()))+1
        else:
            dict[item.upper()] = 1
    except EOFError:
        break

dict_sorted = {key: value for key, value in sorted(dict.items())}
for value in dict_sorted.keys():
    print(str(dict_sorted[value]) + " " + value)