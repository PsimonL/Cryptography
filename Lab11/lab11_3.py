from Crypto.Hash import HMAC, SHA256, SHA512, SHA3_256, SHA3_512


def compute_hmac(message, key, hash_function):
    hmac_obj = HMAC.new(key.encode(), msg=message.encode(), digestmod=hash_function)
    return hmac_obj.hexdigest()


def validate_hmac(message, key, provided_hmac, hash_function):
    try:
        hmac_obj = HMAC.new(key.encode(), msg=message.encode(), digestmod=hash_function)
        hmac_obj.hexverify(provided_hmac)
        return True
    except ValueError:
        return False


def print_validation(message, key, provided_hmac, hash_function):
    is_authentic = validate_hmac(message, key, provided_hmac, hash_function)
    print(f"The message '{message}' is authentic: {is_authentic}")


def print_hmac_results():
    message = "The quick brown fox jumps over the lazy dog"  # brown
    key = "key"

    hmac_sha256 = compute_hmac(message, key, SHA256)
    hmac_sha512 = compute_hmac(message, key, SHA512)
    hmac_sha3_256 = compute_hmac(message, key, SHA3_256)
    hmac_sha3_512 = compute_hmac(message, key, SHA3_512)

    print(f"HMAC-SHA256: {hmac_sha256}")
    print(f"HMAC-SHA512: {hmac_sha512}")
    print(f"HMAC-SHA3-256: {hmac_sha3_256}")
    print(f"HMAC-SHA3-512: {hmac_sha3_512}")

    print("\nValidating HMACs:")
    print_validation(message, key, hmac_sha256, SHA256)

    tampered_message = "The quick brwon fox jumps over the lazy dog"  # brwon
    print_validation(tampered_message, key, hmac_sha256, SHA256)


if __name__ == "__main__":
    print_hmac_results()
