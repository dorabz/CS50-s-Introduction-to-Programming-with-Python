
def convert(str):
    replaced = text.replace(":)", "🙂").replace(":(", "🙁")
    return replaced



if __name__ == "__main__":
    text = input("Insert text with a face:")
    print(convert(text))
