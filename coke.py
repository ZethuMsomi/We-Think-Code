def coke():
    amount = 0
    price = 50

    while amount < price:
        print("Amount Due:", price - amount)
        money = int(input("Insert a coin:"))
        if money in [5, 10, 25]:
            amount += money

    change = amount - price
    print("Change Owed:", change)

coke()
