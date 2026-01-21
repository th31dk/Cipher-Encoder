message = str(input('What message would you like to encode?')).upper()
validCipher = False

while validCipher == False:
    cipherType = str(input("What Cipher would you like to use?")).upper()
    
    if cipherType == "ATBASH":
        validCipher = True
        ATBASH = {'A':'Z', 'B':'Y', 'C':'X', 'D':'W', 'E':'V', 'F':'U', 'G':'T', 'H':'S', 'I':'R', 'J':'Q', 'K':'P', 'L':'O', 'M':'N',
                'N':'M', 'O':'L', 'P':'K', 'Q':'J', 'R':'I', 'S':'H', 'T':'G', 'U':'F', 'V':'E', 'W':'D', 'X':'C', 'Y':'B', 'Z':'A'}
        def ATBASHencode(message):
            cipher = ''
            for characters in message:
                if characters == ' ':
                    cipher += ' '
                else:
                    cipher += ATBASH[characters]
            return cipher
        encodedMessage = ATBASHencode(message)

    elif cipherType == "CAESAR":
        validCipher = True
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        def CAESARencode(message):
            shift = int(input("What shift?")) % 26
            cipherKey = alphabet[shift:] + alphabet[:shift]
            encode = str.maketrans(alphabet, cipherKey)
            cipher = message.translate(encode)
            return cipher
        encodedMessage = CAESARencode(message)

    elif cipherType == "BINARY":
        validCipher = True
        def BINARYencode(message):
            cipher = ''
            for character in message:
                cipher += str(bin((ord(character))))[2:]
            return cipher
        encodedMessage = BINARYencode(message)

    elif cipherType == "VIGENERE":
        validCipher = True
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabetValues = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13,
                          'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23,'X' : 24,'Y' : 25, 'Z' : 26}
        def VIGENEREencode(message):
            cipherKey = input("What keyword would you like to use?").upper()
            keywordLength = 0

            for characters in cipherKey:
            keywordLength += 1

            for characters in message:
                characterNumber = -1
                characterNumber += 1 % keywordLength
                caesar = alphabet[keywordLength:] + alphabet[:keywordLength]
                encode = str.maketrans(alphabet, caesar)
                cipher = message.translate(encode)
                return cipher
        encodedMessage = VIGENEREencode(message)

    else:
        print('INVALID CIPHER TYPE, PLEASE TRY AGAIN')

print('ENCODED MESSAGE:')
print(encodedMessage)