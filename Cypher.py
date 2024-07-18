def caesar_cipher(text, shift):
    result = ""
    shift = shift % 26  # Ensure shift is within mod 26
    
    print("Encryption Steps:")
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            original_position = ord(char) - shift_base
            new_position = (original_position + shift) % 26
            encrypted_char = chr(new_position + shift_base)
            result += encrypted_char
            print(f"{char} -> {original_position} + {shift} = {new_position} -> {encrypted_char}")
        else:
            result += char

    return result

def caesar_decipher(text, shift):
    result = ""
    shift = shift % 26  # Ensure shift is within mod 26
    
    print("Decryption Steps:")
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_position = ord(char) - shift_base
            original_position = (encrypted_position - shift) % 26
            decrypted_char = chr(original_position + shift_base)
            result += decrypted_char
            print(f"{char} -> {encrypted_position} - {shift} = {original_position} -> {decrypted_char}")
        else:
            result += char

    return result

# Get input from the user
text = input("Enter text to be encrypted: ")
shift = int(input("Enter shift value: "))

# Encrypt the text using the Caesar Cipher
encrypted_text = caesar_cipher(text, shift)
print("Encrypted Text: ", encrypted_text)

# Decrypt the text using the Caesar Cipher
decrypted_text = caesar_decipher(encrypted_text, shift)
print("Decrypted Text: ", decrypted_text)
