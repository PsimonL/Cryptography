import hashlib
# from Crypto.Hash import SHA3_224, SHA3_256, SHA3_384, SHA3_512, SHAKE128, SHAKE256

def sha_3_runner(inputt):
    sha3_224 = hashlib.sha3_224(inputt).hexdigest()
    sha3_256 = hashlib.sha3_256(inputt).hexdigest()
    sha3_384 = hashlib.sha3_384(inputt).hexdigest()
    sha3_512 = hashlib.sha3_512(inputt).hexdigest()
    shake128_256 = hashlib.shake_128(inputt).hexdigest(32)
    shake128_512 = hashlib.shake_128(inputt).hexdigest(64)
    shake256_512 = hashlib.shake_256(inputt).hexdigest(64)

    # sha3_224_hash = SHA3_224.new(data=input_data).hexdigest()
    # sha3_256_hash = SHA3_256.new(data=input_data).hexdigest()
    # sha3_384_hash = SHA3_384.new(data=input_data).hexdigest()
    # sha3_512_hash = SHA3_512.new(data=input_data).hexdigest()
    # shake128_256_hash = SHAKE128.new(data=input_data).read(32).hex()
    # shake128_512_hash = SHAKE128.new(data=input_data).read(64).hex()
    # shake256_512_hash = SHAKE256.new(data=input_data).read(64).hex()

    print(f"SHA3-224:\n{sha3_224}")
    print(f"SHA3-256:\n{sha3_256}")
    print(f"SHA3-384:\n{sha3_384}")
    print(f"SHA3-512:\n{sha3_512}")
    print(f"SHAKE128 (256-bit):\n{shake128_256}")
    print(f"SHAKE128 (512-bit):\n{shake128_512}")
    print(f"SHAKE256 (512-bit):\n{shake256_512}")


if __name__ == "__main__":
    inputt = b''
    sha_3_runner(inputt)
