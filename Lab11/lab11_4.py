from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def blake2s_256(input_data: str):
    digest = hashes.Hash(hashes.BLAKE2s(32), backend=default_backend())
    digest.update(input_data.encode('utf-8'))
    return digest.finalize().hex()

def blake2b_512(input_data: str):
    digest = hashes.Hash(hashes.BLAKE2b(64), backend=default_backend())
    digest.update(input_data.encode('utf-8'))
    return digest.finalize().hex()


def display_results(input_1, input_2, input_3):
    print(f'BLAKE2s-256("{input_1}", 256):\n{blake2s_256(input_1)}')
    print(f'BLAKE2s-256("{input_2}", 256):\n{blake2s_256(input_2)}')
    print(f'BLAKE2s-256("{input_3}", 256):\n{blake2s_256(input_3)}')

    print()

    print(f'BLAKE2b-512("{input_1}", 512):\n{blake2b_512(input_1)}')
    print(f'BLAKE2b-512("{input_2}", 512):\n{blake2b_512(input_2)}')
    print(f'BLAKE2b-512("{input_3}", 512):\n{blake2b_512(input_3)}')

if __name__ == "__main__":
    input_1 = "The quick brown fox jumps over the lazy dog"
    input_2 = "The quick brown fox jumps over the lazy dof"
    input_3 = "" 
    
    display_results(input_1, input_2, input_3)