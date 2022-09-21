import sys
from os.path import splitext
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("No of args not good")
input = sys.argv[1]
output = sys.argv[2]

print(input +" " + output)

if input.lower().endswith((".jpeg", ".png", ".jpg")) == False:
    sys.exit("Not right kind of file")

if output.lower().endswith((".jpeg", ".png",".jpg")) == False:
    sys.exit("Not right kind of file")

if input.lower().endswith(".jpeg") != output.lower().endswith(".jpeg"):
    sys.exit("Not matching")

if input.lower().endswith(".png") != output.lower().endswith(".png"):
    sys.exit("Not matching")

if input.lower().endswith(".jpg") != output.lower().endswith(".jpg"):
    sys.exit("Not matching")

try:
    image = Image.open(input)
    shirt = Image.open("shirt.png")
    size = shirt.size
    image = ImageOps.fit(image, size)
    image.paste(shirt, shirt)
    image.save(output)

except FileNotFoundError:
        sys.exit("File is not found")
