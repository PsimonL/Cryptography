def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_base = ord('A')
            result += chr((ord(char.upper()) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def cipher_key_3(txt):
    encrypted = ''
    for i in range(0, len(txt), 3):
        group = txt[i:i+3]
        encrypted += group
    return caesar_cipher(encrypted, 3)

def decypher_key_3(txt):
    decrypted = caesar_cipher(txt, -3)
    result = ''
    for i in range(0, len(decrypted), 3):
        group = decrypted[i:i+3]
        result += group
    return result.lower()  

txt_to_encrypt = "attackatonce"

encrypted_txt = cipher_key_3(txt_to_encrypt)
decrypted_txt = decypher_key_3(encrypted_txt)

print("Encryption")
print("Plaintext: ", txt_to_encrypt)
print("Cyphertext:", encrypted_txt)  

print("Decryption")
print("Plaintext: ", encrypted_txt)
print("Cyphertext:", decrypted_txt) 
