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


def find_caesar_shift(char_cipher: str, char_plain: str) -> int:
    """
    Find the Caesar cipher shift by comparing the most common letter in the
    ciphertext with the most common letter in the English language.
    """
    return (ord(char_cipher) - ord(char_plain)) % 26


ciphertext = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
english_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

cipher_frequency = get_letter_frequency(ciphertext)

sorted_cipher_letters = [item[0] for item in cipher_frequency.most_common()]

mapping = {}
for i in range(len(sorted_cipher_letters)):
    mapping[sorted_cipher_letters[i]] = english_frequency[i]

decrypted_message = decrypt_with_mapping(ciphertext, mapping)

print("Ciphertext:", ciphertext)
print("Letter frequency in ciphertext:", cipher_frequency)
print("Decryption mapping:", mapping)
print("Decrypted message using frequency analysis:", decrypted_message.lower())

most_common_cipher_letter = sorted_cipher_letters[0]
most_common_english_letter = english_frequency[0]

shift = find_caesar_shift(most_common_cipher_letter, most_common_english_letter)
print(f"\nMost possible Caesar cipher shift (key): {shift}")

print("\nPotential decryptions for all possible shifts:")
for key in range(26):
    decrypted_text = decrypt_caesar_shift(ciphertext, key)
    print(f"Shift {key}: {decrypted_text.lower()}")
