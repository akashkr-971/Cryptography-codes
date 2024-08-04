def creatematrix(key):
    alphabets = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = key.upper()
    key = key.replace(' ', '')
    key = key.replace('J', 'I')
    matrix_chars = ''
    for char in key + alphabets:
        if char not in matrix_chars:
            matrix_chars += char
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(list(matrix_chars[i:i + 5]))
    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def encryptplayfair(plaintext, matrix, spaces):
    result = ''
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]

    for pos in spaces:
        pos = int(pos)
        result = result[:pos] + ' ' + result[pos:]
    return result

def decryptplayfair(ciphertext, matrix, spaces):
    result = ''
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]

    for pos in spaces:
        pos = int(pos)
        result = result[:pos] + ' ' + result[pos:]
    return result

val = True
while val:
    choice = int(input('Do you want to encrypt (1) or decrypt (2) or exit (3) : '))
    if choice == 1:
        plaintext = input("Enter the text to encrypt: ")
        spaces = [pos for pos, char in enumerate(plaintext) if char == ' ']
        plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
        if len(plaintext) % 2 != 0:
            plaintext += 'X'
        key = input("Enter the key: ")
        matrix = creatematrix(key)
        print("5x5 Matrix:")
        for row in matrix:
            print(' '.join(row))
        encrypted_text = encryptplayfair(plaintext, matrix, spaces)
        print(f"\nEncrypted text: {encrypted_text}\n", )
    elif choice == 2:
        ciphertext = input("Enter the text to decrypt: ")
        spaces = [pos for pos, char in enumerate(ciphertext) if char == ' ']
        ciphertext = ciphertext.upper().replace('J', 'I').replace(' ', '')
        key = input("Enter the key: ")
        matrix = creatematrix(key)
        print("5x5 Matrix:")
        for row in matrix:
            print(' '.join(row))
        decrypted_text = decryptplayfair(ciphertext, matrix, spaces)
        print(f"\nDecrypted text: {decrypted_text}\n")
    elif choice == 3:
        print("Exiting.....")
        val=False
        exit()
    else:
        print("Wrong choice please select the correct option.\n")
