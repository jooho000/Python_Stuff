# assignment: programming assignment 3
# author: Jooho Lee
# date: 2/9/2024
# file: convert.py is a program that converts values
# input: user choice (F,M,P) and a float
# output: String value after converting

def format (num, precision = 2):
    myStr = round(num,precision)
    myStr = str(myStr)
    if '.00' in myStr:
        myStr = myStr[:-3]
    if '.0' in myStr and myStr[-1] == '0':
        myStr = myStr[:-2]
    return myStr

def isfloat (token):
    if (type(token) == float):
        return True
    else:
        return False

def fahrenheit_celsius (Fahrenheit):
    Celsius = (Fahrenheit - 32) * 5 / 9
    Fahrenheit= format(Fahrenheit)
    Celsius = format(Celsius)
    print(Fahrenheit + " Fahrenheit corresponds to " + Celsius + " Celsius.\n")

def miles_km (miles):
    km = miles * 1.609344 
    km = format(km)
    miles = format(miles)
    print(miles + " miles corresponds to " + km + " km.\n")

def pounds_kg (pounds):
    kg = pounds * 0.45359237
    pounds = format(pounds)
    kg = format(kg)
    print(pounds + " pounds corresponds to " + kg + " kg.\n")

def doFahrenheit():
    while True:     
        try:
            clientNum = float(input("Please enter a temperature in Fahrenheit:\n"))
            fahrenheit_celsius(clientNum)
            clientChoice = input("Do you want to continue? [Y/N]:\n")
            if clientChoice == 'Y' or clientChoice == 'y':
                return True
            elif clientChoice == 'N' or clientChoice == 'n':
                return False
        except ValueError:
            print("You did not enter a number.\n")

def doPound():
    while True:
        try:
            clientNum = float(input("Please enter pounds:\n"))
            pounds_kg(clientNum)
            clientChoice = input("Do you want to continue? [Y/N]:\n")
            if clientChoice == 'Y' or clientChoice == 'y':
                return True
            elif clientChoice == 'N' or clientChoice == 'n':
                return False
        except ValueError:
            print("You did not enter a number.\n")

def doMiles():
    while True:
        try:
            clientNum = float(input("Please enter miles:\n"))
            miles_km(clientNum)
            clientChoice = input("Do you want to continue? [Y/N]:\n")
            if clientChoice == 'Y' or clientChoice == 'y':
                return True
            elif clientChoice == 'N' or clientChoice == 'n':
                return False
        except ValueError:
            print("You did not enter a number.\n")

print("Welcome to the SI Unit Converter!\n")
continueLoop = True
while continueLoop == True:
    print("Please choose one of the following conversions:\n")
    print("Fahrenheit to Celsius - F\n")
    print("Pounds to kg - P\n")
    print("Miles to km - M\n")
    unserInput = input()

    if unserInput == 'F' or unserInput == 'f':
        continueLoop = doFahrenheit()
    elif unserInput == 'P' or unserInput == 'p':
        continueLoop = doPound()
    elif unserInput == 'M' or unserInput == 'm':
        continueLoop = doMiles()
    else:
        print("You did not choose correctly.\n")
        continue

print("Goodbye!")