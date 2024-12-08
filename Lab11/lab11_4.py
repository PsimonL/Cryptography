import hashlib


def sha3_224_empty_string(input_data):
    hash_result = hashlib.sha3_224(input_data).hexdigest()
    print(f"SHA3-224 for {input_data}: {hash_result}")


if __name__ == "__main__":
    input_data = b""
    sha3_224_empty_string(input_data)
    # https://keccak.team/keccak_specs_summary.html
