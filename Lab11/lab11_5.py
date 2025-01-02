from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend


def compute_hmac(message, key, hash_function):
    h = hmac.HMAC(key.encode(), hash_function(), backend=default_backend())
    h.update(message.encode())
    return h.finalize().hex()


def validate_hmac(message, key, provided_hmac, hash_function):
    try:
        h = hmac.HMAC(key.encode(), hash_function(), backend=default_backend())
        h.update(message.encode())
        h.verify(bytes.fromhex(provided_hmac))
        return True
    except Exception:  
        return False


def print_validation(message, key, provided_hmac, hash_function, hash_name):
    is_authentic = validate_hmac(message, key, provided_hmac, hash_function)
    indicator = ""
    if is_authentic == True:
        indicator = ""
    else:
        indicator = " NOT"
    print(f"The message '{message}' is{indicator} authentic for key = [{key}] using {hash_name}.")


def print_hmac_results():
    message = "The quick brown fox jumps over the lazy dog"
    key = "key"  
    tampered_key = "abc" 
    tampered_message_1 = "The quick brwon fox jumps over the lazy dog" 
    tampered_message_2 = "The quick brown fox jumps over the lazy dof" 

    hmac_sha256 = compute_hmac(message, key, hashes.SHA256)
    hmac_sha512 = compute_hmac(message, key, hashes.SHA512)
    hmac_sha3_256 = compute_hmac(message, key, hashes.SHA3_256)
    hmac_sha3_512 = compute_hmac(message, key, hashes.SHA3_512)

    print(f"HMAC-SHA256:\n{hmac_sha256}\n")
    print(f"HMAC-SHA3-256:\n{hmac_sha3_256}\n")
    print(f"HMAC-SHA512:\n{hmac_sha512}\n")
    print(f"HMAC-SHA3-512:\n{hmac_sha3_512}\n")

    print("\nValidating HMACs:")
    print_validation(tampered_message_1, tampered_key, hmac_sha3_512, hashes.SHA3_512, "HMAC SHA3-512")
    print_validation(message, key, hmac_sha3_512, hashes.SHA3_512, "HMAC SHA3-512")
    print_validation(tampered_message_2, key, hmac_sha3_512, hashes.SHA3_512, "HMAC SHA3-512")

if __name__ == "__main__":
    print_hmac_results()
