def encryptceaser(a,b):
    result = ''
    for char in a:
        if char.isupper():
            index = alphabets_upper.index(char)
            new_index = (index + b ) % 26
            result += alphabets_upper[new_index]
        elif char.islower():
            index = alphabets_lower.index(char)
            new_index = (index + b ) % 26
            result += alphabets_lower[new_index]
        elif char == ' ':
            result += ' '
        else:
            result+=char
    return result

def decryptceaser(a,b):
    result = ''
    for char in a:
        if char.isupper():
            index = alphabets_upper.index(char)
            new_index = (index - b ) % 26
            result += alphabets_upper[new_index]
        elif char.islower():
            index = alphabets_lower.index(char)
            new_index = (index - b ) % 26
            result += alphabets_lower[new_index]
        elif char == ' ':
            result += ' '
        else:
            result+=char
    return result

alphabets_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets_lower='abcdefghijklmnopqrstuvwxyz'
choice = int(input('Do you want to encrypt (1) or decrypt (2) : '))
if choice == 1:
    a = input("Enter the string to encrypt : ")
    b = int(input("Enter the key to shift : "))
    encrypted = encryptceaser(a,b)
    print(f'The Encrypted cipher text is : {encrypted}')
elif choice == 2: 
    a = input("Enter the string to decrypt : ")
    b = int(input("Enter the key to shift : "))
    decrypted = decryptceaser(a,b)
    print(f'The Decrypted cipher text is : {decrypted}')

