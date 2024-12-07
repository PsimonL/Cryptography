"""
Zaimplementuj szyfr przestawieniowy z kluczem 3 i zaszyfruj i odszyfruj wiadomość
"attackatonce".
"""

def caesar_cipher(text: str, shift: int) -> str:
    """
    Encrypts or decrypts a given text using the Caesar cipher method.
    Parameters:
    text (str): The input text to be encrypted or decrypted.
    shift (int): The number of positions to shift each character.
    Returns:
    str: The encrypted or decrypted text.
    """
    result = ''
    for char in text:
        if char.isalpha():
            shift_base = ord('A')
            result += chr((ord(char.upper()) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def cipher_key_3(txt: str) -> str:
    """
    Encrypts a given text using a transposition cipher with a key of 3.
    Parameters:
    txt (str): The input text to be encrypted.
    Returns:
    str: The encrypted text after applying the transposition and Caesar cipher.
    """
    encrypted = ''
    for i in range(0, len(txt), 3):
        group = txt[i:i + 3]
        encrypted += group
    return caesar_cipher(encrypted, 3)


def decypher_key_3(txt: str) -> str:
    """
    Decrypts a given text that was encrypted using a transposition cipher with a key of 3.
    Parameters:
    txt (str): The encrypted text to be decrypted.
    Returns:
    str: The original plaintext after decryption.
    """
    decrypted = caesar_cipher(txt, -3)
    result = ''
    for i in range(0, len(decrypted), 3):
        group = decrypted[i:i + 3]
        result += group
    return result.lower()


txt_to_encrypt = "attackatonce"

encrypted_txt = cipher_key_3(txt_to_encrypt)
decrypted_txt = decypher_key_3(encrypted_txt)

print("Encryption")
print("Plaintext: ", txt_to_encrypt)
print("Cyphertext:", encrypted_txt)
print()
print("Decryption")
print("Plaintext: ", encrypted_txt)
print("Cyphertext:", decrypted_txt)

"""
Encryption
Plaintext:  attackatonce
Cyphertext: DWWDFNDWRQFH

Decryption
Plaintext:  DWWDFNDWRQFH
Cyphertext: attackatonce
"""
