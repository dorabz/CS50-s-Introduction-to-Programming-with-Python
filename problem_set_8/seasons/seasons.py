from datetime import date
import inflect, sys

i = inflect.engine()
factor = 24*60

def main():
    dob = input("DOB:")
    try:
        dob1 = date.fromisoformat(dob)
        dob2 = (date.today() - dob1).days*factor
        #print(dob2)
        text = textualize(dob2)
        print(text.capitalize() + " minutes")

    except Exception:
        sys.exit("Exit")


def textualize(dob2):
    return i.number_to_words(dob2, andword="")


if __name__ == "__main__":
    main()