def main():
    greeting = input("Listening for a greeting...")
    str = value(greeting)
    print(str)

def value(greeting):
    if greeting.strip().lower().startswith("hello"):
        return 0
    elif greeting.strip().lower().startswith("h") and not greeting.strip().lower().startswith("hello"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()