greeting = input("Listening for a greeting...")
if greeting.strip().lower().startswith("hello"):
    print("$0")
elif greeting.strip().lower().startswith("h") and not greeting.strip().lower().startswith("hello"):
    print("$20")
else:
    print("$100")