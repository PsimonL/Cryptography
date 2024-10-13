"""
Użyj wyczerpującego wyszukiwania klucza, aby odszyfrować następujący szyfrogram,
który został zaszyfrowany przy użyciu szyfru przestawieniowego
BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD
Jaka jest wartość klucza?
"""


def decrypt_caesar(ciphertext, shift):
    decrypted_text = ''

    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char

    return decrypted_text


ciphertext = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"

possible_shifts = range(1, 26)

for shift in possible_shifts:
    decrypted_text = decrypt_caesar(ciphertext, shift)
    print(f'Shift: {shift} ; Deciphered text: {decrypted_text.lower()}')

print(f'\n Answer for shift = {possible_shifts[9]} and deciphered text = {(decrypt_caesar(ciphertext, possible_shifts[9])).lower()}')
