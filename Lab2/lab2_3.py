"""
Sprawdź, ile możliwych kluczy należy wypróbować w średniej, aby odszyfrować
szyfrogram zaszyfrowany szyfrem przestawieniowym?
Wygeneruj losowy tekst jawny.
Zaszyfruj go losowym kluczem.
Znajdź klucz przy użyciu metody wyczerpującego wyszukiwania.
Uśrednij liczbę prób po 1000 losowych tekstów jawnych.
"""

import random
import string


def encrypt_caesar(plaintext: str, shift: int) -> str:
    """
    Encrypts or decrypts a given text using the Caesar cipher method.
    Parameters:
    plaintext (str): The input text to be encrypted or decrypted.
    shift (int): The number of positions to shift each character.
    Returns:
    str: The encrypted or decrypted text.
    """
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int) -> str:
    """
    Decrypts the given ciphertext using Caesar cipher by reversing the shift.
    Parameters:
    ciphertext (str): The encrypted message to be decrypted.
    shift (int): The number of positions to reverse shift each character.
    Returns:
    str: The resulting plaintext after decrypting the Caesar cipher.
    """
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text


def brute_force_caesar():
    """
    Attempts to find the key used in the Caesar cipher by brute force. This
    function performs 1000 tests, each with a randomly generated plaintext
    and a randomly selected Caesar cipher key.
    Returns:
    tuple[float, int]:
    - average_attempts (float): The average number of attempts needed to find the correct key.
    - total_attempts (int): The total number of attempts across all tests.
    """
    total_attempts = 0
    for _ in range(num_tests):
        plaintext = generate_random_plaintext()
        random_shift = random.randint(0, 25)

        ciphertext = encrypt_caesar(plaintext, random_shift)

        """
        Brute force search to find the correct shift used to encrypt the ciphertext.
        """
        for shift in range(26):
            """
            Check if the current shift correctly decrypts the ciphertext to the original plaintext.
            """
            if decrypt_caesar(ciphertext, shift) == plaintext:
                total_attempts += shift + 1
                break

    average_attempts = total_attempts / num_tests

    return average_attempts, total_attempts


def generate_random_plaintext(length=100):
    """
    Generates a random plaintext consisting of uppercase letters.
    Parameters:
    length (int, optional): The length of the generated plaintext. Defaults to 100.
    Returns:
    str: The randomly generated plaintext string.
    """
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


num_tests = 1000

print("Average number of tries to find correct key, "
      "after perfoming Caesar cipher, after 1000 tests, "
      "using random brute force method.")

average, attempts = brute_force_caesar()
print(f"Average = {average} for total attempts = {attempts} and number of tests {num_tests}")
