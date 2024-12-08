import hashlib


def compute_shake128_hash(input_string, output_bits=256):
    shake128_hash = hashlib.shake_128(input_string.encode()).hexdigest(output_bits // 8)
    return shake128_hash


def display_avalanche_effect():
    input_1 = "The quick brown fox jumps over the lazy dog"
    input_2 = "The quick brown fox jumps over the lazy dof"  # Changed "g" to "f"

    hash_1 = compute_shake128_hash(input_1, 256)
    hash_2 = compute_shake128_hash(input_2, 256)

    print(f"SHAKE-128(\"{input_1}\", 256): {hash_1}")
    print(f"SHAKE-128(\"{input_2}\", 256): {hash_2}")


if __name__ == "__main__":
    display_avalanche_effect()
