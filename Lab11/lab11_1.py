from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def sha_3_runner(input_data):
    digest = hashes.Hash(hashes.SHA3_224(), backend=default_backend())
    digest.update(input_data)
    sha3_224_hash = digest.finalize().hex()

    digest = hashes.Hash(hashes.SHA3_256(), backend=default_backend())
    digest.update(input_data)
    sha3_256_hash = digest.finalize().hex()

    digest = hashes.Hash(hashes.SHA3_384(), backend=default_backend())
    digest.update(input_data)
    sha3_384_hash = digest.finalize().hex()

    digest = hashes.Hash(hashes.SHA3_512(), backend=default_backend())
    digest.update(input_data)
    sha3_512_hash = digest.finalize().hex()

    shake128 = hashes.Hash(hashes.SHAKE128(32), backend=default_backend())  # 32 bytes = 256 bits
    shake128.update(input_data)
    shake128_256_hash = shake128.finalize().hex()

    shake128 = hashes.Hash(hashes.SHAKE128(64), backend=default_backend())  # 64 bytes = 512 bits
    shake128.update(input_data)
    shake128_512_hash = shake128.finalize().hex()

    shake256 = hashes.Hash(hashes.SHAKE256(64), backend=default_backend())  # 64 bytes = 512 bits
    shake256.update(input_data)
    shake256_512_hash = shake256.finalize().hex()

    print(f"SHA3-224 ('{input_data}'):\n{sha3_224_hash}")
    print(f"SHA3-256 ('{input_data}'):\n{sha3_256_hash}")
    print(f"SHA3-384 ('{input_data}'):\n{sha3_384_hash}")
    print(f"SHA3-512 ('{input_data}'):\n{sha3_512_hash}")
    print(f"SHAKE128 (256-bit) ('{input_data}'):\n{shake128_256_hash}")
    print(f"SHAKE128 (512-bit) ('{input_data}'):\n{shake128_512_hash}")
    print(f"SHAKE256 (512-bit) ('{input_data}'):\n{shake256_512_hash}")


if __name__ == "__main__":
    inputt = b''
    sha_3_runner(inputt)
