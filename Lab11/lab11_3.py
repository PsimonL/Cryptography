import random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import matplotlib.pyplot as plt
import numpy as np


def generate_random_512bit_number():
    return random.getrandbits(512)


def flip_random_bit(number, bit_length=512):
    random_bit = 1 << random.randint(0, bit_length - 1)
    return number ^ random_bit


def compute_sha3_512_digest(number):
    number_bytes = number.to_bytes(64, byteorder="big")
    digest = hashes.Hash(hashes.SHA3_512(), backend=default_backend())
    digest.update(number_bytes)
    return digest.finalize()


def count_ones_in_xor(hash1, hash2):
    xor_result = int.from_bytes(hash1, byteorder="big") ^ int.from_bytes(hash2, byteorder="big")
    return bin(xor_result).count("1")


def calculate_ksac(iterations=10000):
    ksac_values = []

    for _ in range(iterations):
        # 1: Generate num A
        number_a = generate_random_512bit_number()

        # 2: Change random bit -> num B
        number_b = flip_random_bit(number_a)

        # 3: SHA-3-512 for A and B
        hash_a = compute_sha3_512_digest(number_a)
        hash_b = compute_sha3_512_digest(number_b)

        # 4: XOR and summing up '1' bits
        ones_count = count_ones_in_xor(hash_a, hash_b)

        # 5: Calculate Ksac
        ksac = ones_count / 512
        ksac_values.append(ksac)

    return ksac_values


def plot_histogram(ksac_values):
    plt.figure(figsize=(10, 6))
    plt.hist(ksac_values, bins=53, color='skyblue', edgecolor='black')  # density=True => for normalization and getting probability density as result
    plt.title("Avalanche Effect Factor Histogram: Ksac")
    plt.xlabel("Ksac")
    plt.ylabel("Number of occurrences")  # Probability Density
    plt.axvline(0.5, color='red', linestyle='dashed', linewidth=1, label="Expected Ksac Averages: Ksac = 0.5")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    iterations = 150000
    print(f"Number of iterations =  {iterations}")
    ksac_values = calculate_ksac(iterations)

    mean_ksac = np.mean(ksac_values)
    print(f"Average Ksac value after {iterations} iterations: {mean_ksac:.4f}")

    plot_histogram(ksac_values)
