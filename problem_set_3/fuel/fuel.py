
class Error(Exception):
    """Base class for other exceptions"""
    pass

class NotGoodError(Error):
    pass


while True:
    try:
        br, naz = input("Input fraction: ").split("/")
        if int(br) > int(naz):
            raise NotGoodError
        perc = (int(br)/int(naz))*100
        if perc <=1:
            print("E")
        elif perc >= 99:
            print("F")
        else:
            print(f'{perc:.0f}%')
    except ValueError:
        print("Must be an integer")
    except ZeroDivisionError:
        print("Can't divide with 0")
    except NotGoodError:
        print("Br is bigger than naz!")
    else:
        break
