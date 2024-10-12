"""
Zaimplementuj szyfr Vigenere’a i zaszyfruj i odszyfruj wiadomość
thiscryptosystemisnotsecure z kluczem CIPHER.
"""
def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key_length = len(key)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            p = ord(char) - ord('a') if char.islower() else ord(char) - ord('A')
            k = ord(key[i % key_length].lower()) - ord('a')
            encrypted_char = chr((p + k) % 26 + ord('a')) if char.islower() else chr((p + k) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)

    result = ''.join(encrypted_text)

    return result.upper()


def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            c = ord(char) - ord('a') if char.islower() else ord(char) - ord('A')
            k = ord(key[i % key_length].lower()) - ord('a')
            decrypted_char = chr((c - k + 26) % 26 + ord('a')) if char.islower() else chr((c - k + 26) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)

    result = ''.join(decrypted_text)

    return result.lower()


txt_to_encrypt = "thiscryptosystemisnotsecure"
key = "CIPHER"

encrypted_message = vigenere_encrypt(txt_to_encrypt, key)
decrypted_message = vigenere_decrypt(encrypted_message, key)

print(f"key: {key}")
print("Encryption")
print("Plaintext: ", txt_to_encrypt)
print("Cyphertext:", encrypted_message)

print("\nDecryption")
print("Plaintext: ", decrypted_message)
print("Cyphertext:", encrypted_message)

"""
key: CIPHER
Encryption
Plaintext:  thiscryptosystemisnotsecure
Cyphertext: VPXZGIAXIVWPUBTTMJPWIZITWZT

Decryption
Plaintext:  thiscryptosystemisnotsecure
Cyphertext: VPXZGIAXIVWPUBTTMJPWIZITWZT
"""
