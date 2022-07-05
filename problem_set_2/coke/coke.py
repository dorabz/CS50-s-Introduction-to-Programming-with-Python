
print("Amount due: 50")

amount_due = 50
coin = 0
list = [25, 10, 5]
while (amount_due > 0):
    coin = int(input("Insert coin: "))
    if coin in list:
        amount_due -= coin
    if amount_due > 0:
        print("Amount due:" + str(amount_due))
print("Change owed:" + str(abs(amount_due)))
