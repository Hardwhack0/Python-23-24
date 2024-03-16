def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value for Caesar cipher: "))

encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)