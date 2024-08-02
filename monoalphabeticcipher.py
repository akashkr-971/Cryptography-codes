def encryptmono(a):
    result = ''
    for char in a:
        if char.isupper():
            text_index = alphabets_upper.index(char)
            result += key_upper[text_index]
        elif char.islower():
            text_index = alphabets_lower.index(char)
            result += key_lower[text_index]
        elif char == ' ':
            result+=' '
    return result

def decryptmono(a):
    result= ''
    for char in a:
        if char.isupper():
            text_index = key_upper.index(char)
            result += alphabets_upper[text_index]
        elif char.islower():
            text_index = key_lower.index(char)
            result += alphabets_lower[text_index]
        elif char == ' ':
            result+=' '
    return result

alphabets_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets_lower='abcdefghijklmnopqrstuvwxyz'
key_upper='QWERTYUIOPASDFGHJKLZXCVBNM'
key_lower='qwertyuiopasdfghjklzxcvbnm'
choice = int(input('Do you want to encrypt (1) or decrypt (2) : '))
if choice == 1:
    a = input("Enter the string to encrypt : ")
    encrypted = encryptmono(a)
    print(f'The Encrypted cipher text is : {encrypted}')
elif choice == 2: 
    a = input("Enter the string to decrypt : ")
    decrypted = decryptmono(a)
    print(f'The Decrypted cipher text is : {decrypted}')

