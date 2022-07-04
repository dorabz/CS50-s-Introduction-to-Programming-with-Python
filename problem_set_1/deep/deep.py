answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if answer == "forty-two" or answer == "forty two" or answer == "42" or answer.lower() == "forty two" or answer.strip() == "42":
    print("Yes")
else:
    print("No")