dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

counter = 0
while True:
    try:
        order = input("What's your order?")
        if order.title() in dict:
            counter += dict.get(order.title())
    except EOFError:
        break
    finally:
        print(f'${counter:.2f}')


