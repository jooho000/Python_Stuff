# assignment: programming assignment 4
# author: Jooho Lee
# date: 2/24/2024
# file: cipher.py is a program that does cipher
# input: filenames
# output: ecypted or decrypted messages

def readfile():
    while True:
        try:
            readfileName = input("Please enter a file for reading:\n")
            file1 = open(readfileName,'r')
            break
        except FileNotFoundError:
            print("The selected file cannot be open for reading!")
    Lines = file1.readlines()
    file1.close()
    return Lines

def writefile(message):
    while True:
        try:
            writefileName = input("Please enter a file for writing:\n")
            file1 = open(writefileName,'w')
            break
        except FileNotFoundError:
            print("The selected file cannot be open for writing!")
    file1.writelines(message)
    file1.close()

def makeAlphabet():
    myAlphabet = []
    for i in range(26):
        char = i + 65
        myAlphabet.append(chr(char))
    return myAlphabet

def encode(plainText, shift = 3):
    myAlphabet = makeAlphabet()
    ListToReturn = []
    for x in range(0,len(plainText)):
        tempString = ""
        for char in plainText[x]:
            if char in myAlphabet:
                i = myAlphabet.index(char)
                letter = myAlphabet[(i + shift) % len(myAlphabet)]
                tempString += letter
            else:
                tempString += char
        ListToReturn.append(tempString)
    return ListToReturn

def doEncode():
    linesToEncode = readfile()
    encodedLines = encode(linesToEncode)
    writefile(encodedLines)
    print("Plaintext:")
    for x in range(0, len(linesToEncode)):
        linesToEncode[x] = linesToEncode[x].upper()
        print(linesToEncode[x], end="")
    print()
    print("Ciphertext:")
    for x in range(0, len(linesToEncode)):
        print(encodedLines[x], end="")
    print()

def decode(plainText, shift = 3):
    myAlphabet = makeAlphabet()
    ListToReturn = []
    for x in range(0,len(plainText)):
        tempString = ""
        for char in plainText[x]:
            if char in myAlphabet:
                i = myAlphabet.index(char)
                letter = myAlphabet[(i - shift) % len(myAlphabet)]
                tempString += letter
            else:
                tempString += char
        ListToReturn.append(tempString)
    return ListToReturn

def doDecode():
    linesToDecode = readfile()
    decodedLines = decode(linesToDecode)
    writefile(decodedLines)
    print("Ciphertext:")
    for x in range(0, len(linesToDecode)):
        linesToDecode[x] = linesToDecode[x].upper()
        print(linesToDecode[x], end="")
    print()
    print("Plaintext:")
    for x in range(0, len(linesToDecode)):
        print(decodedLines[x], end="")
    print()

if __name__ == '__main__':
    while True:
        print("Would you like to encode or decode the message?")
        userInput = input("Type E to encode, D to decode, or Q to quit: \n")
        if userInput == 'E' or  userInput == 'e':
            doEncode()
        elif userInput == 'D' or  userInput == 'd':
            doDecode()
        elif userInput == 'Q' or userInput == 'q':
            print("Goodbye!")
            break
        else:
            print("enter a valid input ")
