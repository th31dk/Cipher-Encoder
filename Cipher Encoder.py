message = str(input('What message would you like to encode?')).upper()
validCipher = False

while validCipher == False:
    cipherType = str(input("What Cipher would you like to use?(ATBASH or CAESAR)")).upper()
    
    if cipherType == "ATBASH":
        validCipher = True
        ATBASH = {'A':'Z', 'B':'Y', 'C':'X', 'D':'W', 'E':'V', 'F':'U', 'G':'T', 'H':'S', 'I':'R', 'J':'Q', 'K':'P', 'L':'O', 'M':'N',
                'N':'M', 'O':'L', 'P':'K', 'Q':'J', 'R':'I', 'S':'H', 'T':'G', 'U':'F', 'V':'E', 'W':'D', 'X':'C', 'Y':'B', 'Z':'A'}
        def ATBASHencode(message):
            cipher = ''
            for character in message:
                if character == ' ':
                    cipher += ' '
                else:
                    cipher += ATBASH[letter]
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
                cipher += ord(character)
       
        encodedMessage = BINARYencode(message)


    else:
        print('INVALID CIPHER TYPE, PLEASE TRY AGAIN')

print('ENCODED MESSAGE:')
print(encodedMessage)