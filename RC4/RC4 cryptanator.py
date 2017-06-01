##Gareth Clarson - RC4 Steam Cipher - Workshop 4
##CSI2108 - Cryptography
#This only runs in python 2.7.11 (Probably other 2.7 versions as well)

#Define functions
def start_menu():
    print("\n\nWelcome to the RC4 cipherbot\n")
    print(66 * "-")
    print(25 * "=", "MENU", 30 * "="),
    print("\n")
    print(66 * "-")
    print(  "[1] - Encrypt\n\n"
            "[2] - Decrypt\n\n"
            "[5] - Exit")
    print(66 * "-")
    print(66 * "-")

def decrypt():

    data = raw_input("Enter the Cipher Text: ")
    key = raw_input("Enter the key:")

    data1 = data.decode('hex') #This converts the message from Hex to string
    key1 = key.decode('hex') #This converts the key from Hex to String

    S = range(256)
    j = 0
    out = []

    # [KSA PHASE]
    for i in range(256):
        j = (j + S[i] + ord( key1[i % len(key1)] )) % 256
        S[i] , S[j] = S[j] , S[i]

    # [PRGA PHASE]
    i = j = 0
    for char in data1:
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        out.append(unichr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    result = ''.join(out)
    print result



def encrypt():

    data = raw_input("Enter text to encrypt: ")
    key = raw_input("Enter the key:")

    key1 = key.decode('hex')  # This converts the key from Hex to String

    S = range(256)
    j = 0
    out = []

    # [KSA PHASE]
    for i in range(256):
        j = (j + S[i] + ord(key1[i % len(key1)])) % 256
        S[i], S[j] = S[j], S[i]

    # [PRGA PHASE]
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    result = ''.join(out)
    print (result.encode('hex'))


##Main Body of the start menu selection
while True:
    try:
        start_menu()  # Displays the start menu
        choice = float(input("Please select from the following options:\n\n"))

        #Key Generator main body
        # Encrypt Body
        if choice ==1:
            encrypt()

        #Decrypt Body
        elif choice ==2:
            decrypt()

        #Exit Message
        elif choice ==5:
            print(91 * "-")
            print(30 * "-", "Exiting ", 30 * "-")
            print(91 * "-")
            print("Made by Gareth Clarson - 10392634 - Cryptography")
            break
    except ValueError:
        print("Option not available. Try again..")
