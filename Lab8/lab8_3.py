from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import hashlib
from Crypto.Hash import MD4, MD5, SHA1, SHA224, SHA256, SHA384, SHA512

# pip install pycryptodome
# pip install cryptography

hash_algorithms = {
    "MD4": MD4.new,
    "MD5": MD5.new,
    "SHA-1": SHA1.new,
    "SHA-224": SHA224.new,
    "SHA-256": SHA256.new,
    "SHA-384": SHA384.new,
    "SHA-512": SHA512.new
}


def calculate_hashes(sentences):
    results = {}
    for sentence in sentences:
        sentence_results = {}
        for name, func in hash_algorithms.items():
            h = func()
            h.update(sentence.encode())
            sentence_results[name] = h.hexdigest()
        results[sentence] = sentence_results
    return results


def print_outputs(results):
    for sentence, hashes in results.items():
        print(f"Sentence: {repr(sentence)}")
        for algo, digest in hashes.items():
            print(f"{algo}: {digest}")
        print()

def hash_funcs_runner():
    sentences = [
        "The quick brown fox jumps over the lazy dog",
        "The quick brown fox jumps over the lazy cog",
        ""
    ]
    results = calculate_hashes(sentences)
    print_outputs(results)


if __name__ == "__main__":
    hash_funcs_runner()