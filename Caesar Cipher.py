alphabet = 'abcdefghijklmnopqrstuvwxyz'

shift = int(input("What shift?"))
cipherKey = alphabet[shift:] + alphabet[:shift]
encode = str.maketrans(alphabet, cipherKey)

message = input("What message would you like to encode?")

print("ENCODED MESSAGE:")
print(message.translate(encode))
