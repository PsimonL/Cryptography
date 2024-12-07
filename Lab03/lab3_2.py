def generate_key_stream(initial_vector, length):
    z = list(initial_vector)
    stream = z[:]

    for _ in range(length - len(z)):
        new_bit = (z[0] + z[3]) % 2
        z.append(new_bit)
        stream.append(new_bit)
        z.pop(0)

    return stream


def xor_strings(str1, str2):
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(str1, str2))


def format_seq(sequence):
    return ''.join(map(str, sequence))


plaintext = "011001111111000"
initial_vector = [1, 1, 0, 1, 0]

key_stream = generate_key_stream(initial_vector, len(plaintext))
ciphertext = xor_strings(plaintext, format_seq(key_stream))
decrypted_plaintext = xor_strings(ciphertext, format_seq(key_stream))
formatted_key_stream = format_seq(key_stream)

print("Encryption")
print(f"Plaintext:  {plaintext}")
print(f"Key stream: {formatted_key_stream}")
print(f"Ciphertext: {ciphertext}")

print("\nDecryption")
print(f"Ciphertext: {ciphertext}")
print(f"Key stream: {formatted_key_stream}")
print(f"Plaintext:  {decrypted_plaintext}")
