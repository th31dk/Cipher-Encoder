# Global Variables
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetValues = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13,
                  'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23,'X' : 24,'Y' : 25, 'Z' : 26}

# ATBASH
ATBASHdictionary = {'A':'Z', 'B':'Y', 'C':'X', 'D':'W', 'E':'V', 'F':'U', 'G':'T', 'H':'S', 'I':'R', 'J':'Q', 'K':'P', 'L':'O', 'M':'N',
          'N':'M', 'O':'L', 'P':'K', 'Q':'J', 'R':'I', 'S':'H', 'T':'G', 'U':'F', 'V':'E', 'W':'D', 'X':'C', 'Y':'B', 'Z':'A'}
def ATBASH(message):
    cipher = ''
    for characters in message:
        if characters == ' ':
            cipher += ' '
        else:
            cipher += ATBASHdictionary[characters]
    return cipher

# CAESAR
def CAESARencode(message):
    shift = int(input("What shift?")) % 26
    cipherKey = alphabet[shift:] + alphabet[:shift]
    encode = str.maketrans(alphabet, cipherKey)
    cipher = message.translate(encode)
    return cipher

# BINARY
def BINARYencode(message):
                    cipher = ''
                    for character in message:
                        cipher += str(bin((ord(character))))[2:]
                    return cipher

# VIGENERE
def VIGENEREencode(message):
    cipherKey = input("What keyword would you like to use?").upper()
    cipher = ''
    keyIndex = 0

    for character in message:
        if character == ' ':
            cipher += ' '
        else:
            shift = alphabetValues[cipherKey[keyIndex % len(cipherKey)]] - 1

            position = alphabetValues[character] - 1
            newPosition = (position +shift) % 26

            cipher += alphabet[newPosition]

        keyIndex += 1

    return cipher

goodanswer = False
while goodanswer == False:
    encodeordecode = str(input("Would you like to decode or encode?")).upper()
    if encodeordecode == "ENCODE":
        goodanswer = True
        message = str(input("What message would you like to encode?")).upper()
        validCipher = False

        while validCipher == False:
            cipherType = str(input("What Cipher would you like to use?")).upper()
            
            if cipherType == "ATBASH":
                validCipher = True
                encodedMessage = ATBASH(message)

            elif cipherType == "CAESAR":
                validCipher = True
                encodedMessage = CAESARencode(message)

            elif cipherType == "BINARY":
                validCipher = True
                encodedMessage = BINARYencode(message)

            elif cipherType == "VIGENERE":
                validCipher = True
                encodedMessage = VIGENEREencode(message)

            else:
                print('INVALID CIPHER TYPE, PLEASE TRY AGAIN')

        print("ENCODED MESSAGE:")
        print(encodedMessage)
    elif encodeordecode == "DECODE":
        validCipher = False
        while validCipher == False:
            print("ONLY ATBASH DECODING IS AVAILABLE")
            cipherType = input("What cipher is the encoded message in?").upper
            if cipherType == "ATBASH":
                validCipher == True
            else:
                print("INVALID CIPHER, PLEASE TRY AGAIN")
    else:
        print("INVALID OPTION, PLEASE TRY AGAIN")