import os
import time

def EncryptFile(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    
    file = open(filename, "wb")
    file.write(data)
    file.close()

def DecryptFile(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    
    file = open(filename, "wb")
    file.write(data)
    file.close()


key = 0
choice = ""
while choice != "3":
    os.system("cls")
    choice = input(  \
            "Welcome to Tommy's Crypto Program.\n\
            Select one of the following options:\n\
            1. Encrypt File\n\
            2. Decrypt File\n\
            3. Exit Program\n")

    if choice == "":
        print("Sorry, you must select one of the following options")
        time.sleep(3)
    elif choice == "1":
        os.system("cls")
        key = int(input("Enter a private key to encrypt(between 1 - 255): "))
        filename = input("Please enter a filename: ")
        EncryptFile(filename, key)
        print("Success!")
    elif choice == "2":
        os.system("cls")
        key = int(input("Enter your private key: "))
        filename = input("Please enter a filename: ")
        EncryptFile(filename, key)
        print("Success!")