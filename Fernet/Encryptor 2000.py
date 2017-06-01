#Gareth Clarson - AES + Fernet Encryptor 

#Importing Fernet Module
from cryptography.fernet import Fernet

#Define global variables
#Input choice [1] = generate key, [2] = import key, [3] = Encryptor, [4] = Decryptor
def start_menu():
    print("\n\nWelcome to the Fernet Encryptor 2000,\n")
    print (30 * "-", "MENU", 30 * "-"),
    print(66 * "-")
    print(  "[1] - Fernet Key generator\n\n"
            "[2] - Fernet Encryptor\n\n"
            "[5] - Exit")
    print(66 * "-")
    print(66 * "-")

#[1] Key Generator

def key_gen():
    key = Fernet.generate_key()
    return key

#[2] Encryptor
#Same session encryption
def encrypt():
    cipher_format = Fernet(key_gen())
    cipher_text = cipher_format.encrypt(bytes(input("please enter the text you wish to encrypt:\n\n"), 'utf8'))
    print(71 * "-")
    print("congratulations it is now encrypted, here is the cipher text: \n\n", cipher_text)
    input("\n\n Please hit enter to continue")
    print(71 * "-")

    #Decrypting the message
    plain_text = cipher_format.decrypt(cipher_text)
    print("And here is your decrypted message, is this correct??:\n\n")
    return plain_text

#Imported key Encryption
def importEncrypt():
    imported_key = bytes(input("please enter your key which you want to import:\n\n"), 'utf8')
    print("Key Imported successfully!\n\n This is it right?\n\n", imported_key)
    cipher_Import_format = Fernet(imported_key)
    cipher_text_imported = cipher_Import_format.encrypt(bytes(input("please enter the text you wish to encrypt"), 'utf8'))
    print("congratulations it is now encrypted, here is the cipher text: \n\n", cipher_text_imported)
    input("\n\n Please hit enter to continue")
    print(71 * "-")

    # Decrypting the message
    plain_text = cipher_Import_format.decrypt(cipher_text_imported)
    print("And here is your decrypted message, is this correct??:\n\n")
    return plain_text


##Main Body of the start menu selection

while True:
    try:
        start_menu()  # Displays the start menu
        choice = float(input("Please select from the following options:\n\n"))

        #Key Generator main body
        if choice ==1:
            print(75 * "-")
            print(30 * "-", "Key Generator", 30 * "-"),
            print(75 * "-")
            keyGen_choice = str(input("Would you like to continue? \n\n"
                                 "[Y]es, [N]o\n\n").lower())

            if keyGen_choice == 'y':
                   print(75 * "=")
                   print("Here is your key, Don't show it to anyone!: \n")
                   print(key_gen(),"\n")
                   print("please hit 'enter' to continue....")
                   input(75 * "=")
                   continue

            elif keyGen_choice == 'n':
                  print("Going back to main menu....")
                  continue

        #Encrypto Body
        elif choice ==2:
            print(71 * "-")
            print(30 * "-", "ENCRYPTOR", 30 * "-"),
            print(71 * "-")
            print("[1] - Same Session Encryption\n\n"
                  "[2] - Imported key Encryption\n\n")
            encrypt.c = input("Please select from one of the following options:\n")

            if encrypt.c == "1":
                print(encrypt())
                print(75 * "-")
                print(15 * "-", "Exiting Fernet Encryptor 2000", 15 * "-")
                print(75 * "-")
                print("Made by Gareth Clarson - 10392634 - Cryptography")
                break




            elif encrypt.c == "2":
                print(importEncrypt())
                print(75 * "-")
                print(15 * "-", "Exiting Fernet Encryptor 2000", 15 * "-")
                print(75 * "-")
                print("Made by Gareth Clarson - 10392634 - Cryptography")
                break

        #decryptor
        elif choice ==3:
            cipher_Import_format = Fernet(bytes(input("please enter your key which you want to import:"), 'utf8'))
            cipher_text_imported = cipher_Import_format.decrypt(bytes(input("please enter the text you wish to decrypt"), 'utf8'))

            print (cipher_text_imported)


        #Exit Message
        elif choice ==5:
            print(91 * "-")
            print(30 * "-", "Exiting Fernet Encryptor 2000", 30 * "-")
            print(91 * "-")
            print("Made by Gareth Clarson - 10392634 - Cryptography")
            break


    except ValueError:
        print("Option not available. Try again..")
