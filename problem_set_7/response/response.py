from validator_collection import validators

str = input("Input:")
try:
    validators.email(str)
    print("Valid")
except Exception:
    print("Invalid")