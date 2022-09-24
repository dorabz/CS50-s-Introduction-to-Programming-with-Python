# Project - Hangman
import sys, random


def main():
    try:
        ans = input("Do you want to play? YES/NO\n")
        if get_answer(ans):
            word = get_word(random.randrange(0, 9))
            chances = 7
            print("Your word:\n")
            word_in_guess = ["_"] *len(word)
            print(word_in_guess)
            print("\nChances left: " + "🍀"*chances)
            i = 0
            while chances >= 1 and i < len(word):
                x = input("Your guess:\n")
                if x.isalpha() == True:
                    x = x.upper()
                    if word.find(x) != -1:
                        print("\nGood letter\n")
                        i = i + 1
                        word_in_guess = check_letter(word, x, word_in_guess)
                        print(word_in_guess)
                        print("\nChances left: " + "🍀"*chances)
                    else:
                        print("\nWrong letter\n")
                        print(word_in_guess)
                        chances = chances - 1
                        print("\nChances left: " + "🍀"*chances)
                else:
                    print("We are guessing letters!\n")
        if chances == 0:
            print("\nYOU LOST! 😔")
        if i == len(word):
            print("\nYOU WON! 😊")


    except Exception:
        sys.exit("Bye!")

def get_answer(ans):
    list = ["yes", "no"]
    if ans.lower() in list:
        if ans.lower() == "yes":
            print("Let's play!")
            return True
        else:
            print("Sorry to see you go :(")
            return False
    else:
        raise ValueError("Come back next time")


def get_word(i):
    list = ["DIALECT", "HEALTHY", "DONATE", "ELASTIC", "NETWORK", "SECTION", "LIBERTY", "SCOURGIFY", "KINGDOM", "STRANGER"]
    return list[i]


def check_letter(word, x, word_in_guess):
    for index, letter in enumerate(word):
        if letter == x:
            word_in_guess[index] = x
            return word_in_guess



if __name__ == "__main__":
    main()