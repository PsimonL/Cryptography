"""
Użyj analizy częstości, aby odszyfrować następujący szyfrogram, który został
zaszyfrowany przy użyciu szyfru przestawieniowego
BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD
Wykorzystaj tabelę częstości dla języka angielskiego.
ETAOINSHRDLCUMWFGYPBVKJXQZ
"""

import collections


def get_letter_frequency(text: str) -> dict:
    """
    Calculate the frequency of each letter in the given text.
    Returns a dictionary where keys are letters and values are counts.
    """
    frequency = collections.Counter(text)
    return frequency


def decrypt_with_mapping(ciphertext: str, mapping: dict) -> str:
    """
    Decrypt the ciphertext using a letter mapping (substitution cipher).
    Each letter in the ciphertext is replaced by its corresponding letter from the mapping.
    """
    decrypted_text = ''
    for char in ciphertext:
        if char in mapping:
            decrypted_text += mapping[char]
        else:
            decrypted_text += char
    return decrypted_text


def decrypt_caesar_shift(ciphertext: str, shift: int) -> str:
    """
    Decrypt the ciphertext using a Caesar cipher with the given shift.
    The shift is applied in reverse to each letter of the ciphertext.
    """
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text


ciphertext = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
english_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

cipher_frequency = get_letter_frequency(ciphertext)

sorted_cipher_letters = [item[0] for item in cipher_frequency.most_common()]

for k in range(0, 10):
    mapping = {}
    for i in range(len(sorted_cipher_letters)):
        mapping[sorted_cipher_letters[i]] = english_frequency[i + k]

    decrypted_message = decrypt_with_mapping(ciphertext, mapping)

    print("Ciphertext:", ciphertext)
    print("Letter frequency in ciphertext:", cipher_frequency)
    print("Decryption mapping:", mapping)
    print("Decrypted message using frequency analysis:", decrypted_message.lower())

    key_letter = 'Y'
    mapped_letter = mapping[key_letter]
    ascii_key_letter = ord(key_letter)
    ascii_mapped_letter = ord(mapped_letter)
    shift = ascii_key_letter - ascii_mapped_letter

    final_decrypted_message = decrypt_caesar_shift(ciphertext, shift)
    print(f"Final decrypted message with Caesar cipher (shift {shift}): {final_decrypted_message.lower()}")
    print("\n")
