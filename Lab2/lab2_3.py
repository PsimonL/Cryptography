import random
import string


def encrypt_caesar(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text


def brute_force_caesar(ciphertext, plaintext):
    for shift in range(26):
        if decrypt_caesar(ciphertext, shift) == plaintext:
            return shift
    return None


def generate_random_plaintext(length=100):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


num_tests = 1000
total_attempts = 0

for _ in range(num_tests):
    plaintext = generate_random_plaintext()
    random_shift = random.randint(0, 25)

    ciphertext = encrypt_caesar(plaintext, random_shift)

    for shift in range(26):
        if decrypt_caesar(ciphertext, shift) == plaintext:
            total_attempts += shift + 1
            break

average_attempts = total_attempts / num_tests
print(average_attempts)
