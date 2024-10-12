"""
Zaimplementuj szyfr Hilla i zaszyfruj i odszyfruj wiadomość july z kluczem (w postaci macierzy):
|11 8|
|3 7|
"""

import numpy as np


def hill_encrypt(plaintext, key_matrix):
    plaintext_numbers = [ord(char) - ord('a') for char in plaintext]

    cipher_text = ""

    for i in range(0, len(plaintext_numbers), 2):
        vector = np.array([plaintext_numbers[i], plaintext_numbers[i + 1]])
        encrypted_vector = np.dot(vector, key_matrix) % 26
        cipher_text += chr(encrypted_vector[0] + ord('A')) + chr(
            encrypted_vector[1] + ord('A'))

    return cipher_text


def hill_decrypt(ciphertext, key_inv_matrix):
    plaintext = ""

    ciphertext_numbers = [ord(char) - ord('A') for char in ciphertext]

    for i in range(0, len(ciphertext_numbers), 2):
        vector = np.array([ciphertext_numbers[i], ciphertext_numbers[i + 1]])
        decrypted_vector = np.dot(vector, key_inv_matrix) % 26
        plaintext += chr(decrypted_vector[0] + ord('a')) + chr(
            decrypted_vector[1] + ord('a'))

    return plaintext


key_matrix = np.array([[11, 8], [3, 7]])
key_inv_matrix = np.array([[7, 18], [23, 11]])
plaintext = "july"

ciphertext = hill_encrypt(plaintext, key_matrix)
decrypted_text = hill_decrypt(ciphertext, key_inv_matrix)

print("Encryption")
print(f"Plaintext: {plaintext}")
print(f"Cyphertext: {ciphertext}")

print("\nDecryption")
print(f"Plaintext: {decrypted_text}")
print(f"Cyphertext: {ciphertext}")
