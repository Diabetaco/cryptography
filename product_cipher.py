# Global variables to store even and odd letters
even_letters = ""
odd_letters = ""
y1y2 = ""


def encrypt(input_string):
    global even_letters, odd_letters
    odd_letters = input_string[1::2]  # Slicing to get letters at odd indices
    even_letters = input_string[::2]  # Slicing to get letters at even indices
    set_y1y2()
    product_cipher()

def decrypt(input_string):
    # Get the integer equivalent of 'A'
    z1 = value('A')

    # Decryption of the first character
    message = letter((value(input_string[0]) - z1) % 26)
    
    for i in range(1, len(input_string)):
        message += letter((value(input_string[i])-value(message[i-1])) % 26)

    midpoint = len(message) // 2
    first_half = message[:midpoint + len(message) % 2]
    second_half = message[midpoint + len(message) % 2:]

    decrypted = ""
    for i in range(len(first_half)):
        if(len(message)%2 and i == len(first_half)-1):
            decrypted += first_half[i]
        else:
            decrypted += first_half[i] + second_half[i]

    print(decrypted)


def set_y1y2():
    global even_letters, odd_letters, y1y2
    y1y2 = even_letters+odd_letters

def product_cipher():
    global y1y2
    z1=value('A')
    
    ciphertext=letter((z1 + value(y1y2[0]))%26)
    for i in range(1,len(y1y2)):
        ciphertext+=letter((value(y1y2[i])+value(y1y2[i-1]))%26)
    
    print(ciphertext)

def value(letter):
    return (ord(letter)-65)

def letter(value):
    return (chr(value+65))

if __name__ == "__main__":
    # plaintext = "OVERCONSCIENTIOUSNESS"
    # encrypt(plaintext)

    ciphertext = "CWNKEBHBIIVBBRMLFTEGH"
    decrypt(ciphertext)


