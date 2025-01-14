import hashlib
# from Crypto.Hash import MD5, SHA1, SHA224, SHA256, SHA384, SHA512
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# pip install pycryptodome
# pip install cryptography


hash_algorithms = {
    "MD5": hashes.MD5,
    "SHA-1": hashes.SHA1,
    "SHA-224": hashes.SHA224,
    "SHA-256": hashes.SHA256,
    "SHA-384": hashes.SHA384,
    "SHA-512": hashes.SHA512
}


def calculate_hashes(sentences):
    """Oblicza hashe dla podanych zdań przy użyciu różnych algorytmów."""
    results = {}
    for sentence in sentences:
        sentence_results = {}
        for name, hash_algo in hash_algorithms.items():
            try:
                digest = hashes.Hash(hash_algo(), backend=default_backend())
                digest.update(sentence.encode())
                sentence_results[name] = digest.finalize().hex()
            except Exception as e:
                sentence_results[name] = f"Error: {e}"
        results[sentence] = sentence_results
    return results


def print_outputs(results):
    """Wyświetla wyniki w czytelnej formie."""
    for sentence, hashes in results.items():
        print(f"Sentence: {repr(sentence)}")
        for algo, digest in hashes.items():
            print(f"{algo}: {digest}")
        print()


def hash_funcs_runner():
    """Funkcja uruchamiająca proces obliczania hashy dla przykładowych zdań."""
    sentences = [
        "The quick brown fox jumps over the lazy dog",
        "The quick brown fox jumps over the lazy cog",
        ""
    ]
    results = calculate_hashes(sentences)
    print_outputs(results)


if __name__ == "__main__":
    hash_funcs_runner()
