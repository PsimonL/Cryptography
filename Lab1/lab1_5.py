"""
Zaimplementuj szyfr permutacyjny i odszyfruj wiadomość
TGEEMNELNNTDROEOAAHDOETCSHAEIRLM, dla danej permutacji.
"""
def encrypt(plaintext, permutation):
    n = len(permutation)
    blocks = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]
    ciphertext = ""

    for block in blocks:
        if len(block) < n:
            block += ' ' * (n - len(block))
        permuted_block = ''.join(block[permutation[i]-1] for i in range(n))
        ciphertext += permuted_block

    return ciphertext


def decrypt(ciphertext, permutation):
    n = len(permutation)
    blocks = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)]
    plaintext = ""

    for block in blocks:
        inverted_permutation = [0] * n
        for i in range(n):
            inverted_permutation[permutation[i]-1] = block[i]

        plaintext += ''.join(inverted_permutation)

    return plaintext.strip()


permutation = [2, 4, 6, 1, 8, 3, 5, 7]

plaintext = "gentlemendonotreadeachothersmail"
ciphertext = "TGEEMNELNNTDROEOAAHDOETCSHAEIRLM"

encrypted_text = encrypt(plaintext, permutation)
decrypted_text = decrypt(ciphertext, permutation)

print("Decryption:")
print(f"Plaintext: {decrypted_text.lower()}")
print(f"Cyphertext: {ciphertext}")

print("\nEncryption:")
print(f"Cyphertext: {ciphertext}")
print(f"Plaintext: {encrypted_text.lower()}")

"""
Decryption:
Plaintext: etngeelmdnonetordaeathcoesrhlami
Cyphertext: TGEEMNELNNTDROEOAAHDOETCSHAEIRLM

Encryption:
Cyphertext: TGEEMNELNNTDROEOAAHDOETCSHAEIRLM
Plaintext: etegenlmdntneoordahatecoesahlrmi
"""