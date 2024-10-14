def generate_key_stream(initial_vector, length):
    """
    Generates a key stream based on the linear recurrence relation z_{i+5} = (z_i + z_{i+3}) mod 2.

    Parameters:
    initial_vector (list of int): The initial vector [z0, z1, z2, z3, z4] to start the recurrence.
    length (int): The length of the key stream to generate.

    Returns:
    list of int: Generated key stream of specified length.
    """
    z = list(initial_vector)
    stream = z[:]

    for _ in range(length - len(z)):
        new_bit = (z[0] + z[3]) % 2
        z.append(new_bit)
        stream.append(new_bit)
        z.pop(0)

    return stream


def xor_strings(str1, str2):
    """
    Performs XOR operation between two binary strings.

    Parameters:
    str1 (str): The first binary string (e.g., plaintext or ciphertext).
    str2 (str): The second binary string (e.g., key stream).

    Returns:
    str: The result of XOR operation between the two strings.
    """
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(str1, str2))


def format_binary_sequence(sequence):
    """
    Formats a list of binary numbers into a string.

    Parameters:
    sequence (list of int): A list of binary digits (0s and 1s).

    Returns:
    str: A formatted string representing the binary sequence.
    """
    return ''.join(map(str, sequence))


plaintext = "011001111111000"
initial_vector = [1, 1, 0, 1, 0]

key_stream = generate_key_stream(initial_vector, len(plaintext))
ciphertext = xor_strings(plaintext, format_binary_sequence(key_stream))
decrypted_plaintext = xor_strings(ciphertext, format_binary_sequence(key_stream))
formatted_key_stream = format_binary_sequence(key_stream)

print("Encryption")
print(f"Plaintext:  {plaintext}")
print(f"Key stream: {formatted_key_stream}")
print(f"Ciphertext: {ciphertext}")

print("\nDecryption")
print(f"Ciphertext: {ciphertext}")
print(f"Key stream: {formatted_key_stream}")
print(f"Plaintext:  {decrypted_plaintext}")
