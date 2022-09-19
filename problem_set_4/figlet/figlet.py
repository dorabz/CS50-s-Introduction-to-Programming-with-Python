from pyfiglet import Figlet
import sys

figlet1 = Figlet()

if len(sys.argv) == 1:
    str = input("Your text in random font: ")
    print(figlet1.figlet_format(str))
elif len(sys.argv) == 3:
    fonts = figlet1.getFonts()
    if sys.argv[1] in ["-f", "--font"] and str(sys.argv[2]) in fonts:
        myfont=str(sys.argv[2])
        text = input("Your text in random font: ")
        figlet1.setFont(font=myfont)
        print(figlet1.renderText(text))
    else:
        sys.exit("Number of args not good")
else:
    sys.exit("Number of args not good")

