def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    val = False
    if 2 <= len(s) <= 6:
        if s.isalnum():
            if s[0].isalpha() and s[1].isalpha():
                if s.isalpha():
                    val = True
                if s[len(s)-1].isnumeric():
                    if s[len(s)-1].isnumeric() and s[len(s)-2].isalpha():
                        val = False
                    else:
                        for i in range(len(s)):
                            if s[i].isalpha() and s[i+1].isnumeric() and s[i+1] != "0":
                                val = True
    return val

if __name__ == "__main__":
    main()