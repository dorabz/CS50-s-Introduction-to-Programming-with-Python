
class Error(Exception):
    """Base class for other exceptions"""
    pass

class NotGoodError(Error):
    pass

def main():
    fract = input("Input fraction: ")
    fract1 = convert(fract)
    print(gauge(fract1))

def convert(fraction):
    while True:
        try:
            br, naz = fraction.split("/")
            if int(br) > int(naz):
                raise NotGoodError
            perc = (int(br)/int(naz))*100
        except ValueError:
            print("Must be an integer")
        except ZeroDivisionError:
            print("Can't divide with 0")
        except NotGoodError:
            print("Br is bigger than naz!")
        else:
            return perc


def gauge(percentage):
    if percentage <=1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f'{percentage:.0f}%')


if __name__ == "__main__":
    main()