def main():
    saying = input("Saying: ")
    saying_o = shorten(saying)
    print(saying_o)

def shorten(word):
    res = word.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")
    return res


if __name__ == "__main__":
    main()