def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
        
    return S


def stream_generator(plaintext, S):
    i = 0
    j = 0
    keystream = []
    result_ciphered = []

    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        byte_key = S[(S[i] + S[j]) % 256]
        keystream.append(byte_key)
        result_ciphered.append(ord(char) ^ byte_key)

    return keystream, result_ciphered


def rc4(plaintext, key):
    key = [ord(c) for c in key]
    S = KSA(key)
    keystream, result_ciphered = stream_generator(plaintext, S)
    
    return keystream, result_ciphered


plaintexts = ["Attack at dawn", "Plaintext", "pedia"]
keys = ["Secret", "Key", "Wiki"]

for plaintext, key in zip(plaintexts, keys):
    keystream, ciphertext = rc4(plaintext, key)

    keystream_hex = ''.join(f'{byte:02X}' for byte in keystream)
    ciphertext_hex = ''.join(f'{byte:02X}' for byte in ciphertext)

    print("Keystream:", keystream_hex)
    print("Plaintext:", plaintext)
    print("Key:", key)
    print("Ciphertext:", ciphertext_hex)
    print()
