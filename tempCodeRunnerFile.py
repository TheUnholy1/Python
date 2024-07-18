def caesar_cipher(text, shift):
    result = ""
    shift = shift % 26  # Ensure shift is within mod 26
    
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result

# Get input from the user
text = input("Enter text to be encrypted: ")
shift = int(input("Enter shift value: "))

# Encrypt the text using the Caesar Cipher
encrypted_text = caesar_cipher(text, shift)

print("Encrypted Text: ", encrypted_text)
