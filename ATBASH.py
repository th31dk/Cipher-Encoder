message = str(input('What message would you like to encode?')).upper()
validCipher = False

while validCipher == False:
    cipherType = str(input("What Cipher would you like to use?(ATBASH or CA)")).upper()
    
    if cipherType == 'ATBASH':
        validCipher = True
        ATBASH = {'A':'Z', 'B':'Y', 'C':'X', 'D':'W', 'E':'V', 'F':'U', 'G':'T', 'H':'S', 'I':'R', 'J':'Q', 'K':'P', 'L':'O', 'M':'N',
                'N':'M', 'O':'L', 'P':'K', 'Q':'J', 'R':'I', 'S':'H', 'T':'G', 'U':'F', 'V':'E', 'W':'D', 'X':'C', 'Y':'B', 'Z':'A'}
        def ATBASHencode(message):
            cipher = ''
            for letter in message:
                if letter == ' ':
                    cipher += ' '
                else:
                    cipher += ATBASH[letter]
            return cipher
        encodedMessage = ATBASHencode(message)

    else:
        print('INVALID CIPHER TYPE, PLEASE TRY AGAIN')

print('ENCODED MESSAGE:')
print(encodedMessage)