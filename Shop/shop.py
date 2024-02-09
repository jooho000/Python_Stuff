# assignment: programming assignment 2
# author: Jooho Lee
# date: 1/28/2024
# file: shop.py implements a vending machine
# input: strings and numbers (integers)
# output: interactive messages (strings)

def printChange(userMoney,productPrice):
    if productPrice == userMoney:
        return
    print("Your change is:")
    change = userMoney - productPrice
    dollars = change // 100
    change %= 100
    if dollars > 0:
        print(f"Dollars - {dollars}")
        quarters = change // 25
        change %= 25
    if quarters > 0:
        print(f"Quarters - {quarters}")
        dimes = change // 10
        change %= 10
    if dimes > 0:
        print(f"Dimes - {dimes}")
        nickels = change // 5
        change %= 5
    if nickels > 0:
        print(f"Nickels - {nickels}")
    if change > 0:
        print(f"Cents - {change}")

def vendingMachine(userInput) :
    productPrice = 0;
    productName = ""
    userMoney = 0
    if userInput == 1:
        productPrice = 199
        productName = "bottle of water"
    elif userInput == 2:
        productPrice = 215
        productName = "bottle of orange juice"
    else:
        productPrice = 249
        productName = "bottle of iced tea"
    while userMoney < productPrice:
        try:
            userMoney += int(input("Please deposit money (in cents):\n"))
        except ValueError:
            continue
    print(f"You bought a {productName}.")
    printChange(userMoney,productPrice)


print("Vending Machine")
while True:
    print("Please enter what product you want to buy[1-3] or select quit[4]:")
    print("1. A bottle of water - $1.99")
    print("2. A bottle of orange juice - $2.15")
    print("3. A bottle of iced tea - $2.49")
    print("4. Quit")
    try:
        userInput = int(input())
        if userInput <= 0 or userInput > 4:
            print("You made the wrong choice!")
        elif 1 <= userInput <= 3:
            vendingMachine(userInput)
        elif userInput == 4:
            print("Goodbye!")
            break
    except ValueError:
        print("You made the wrong choice!")