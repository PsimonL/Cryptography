from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def calculate_sha1(file_path):
    digest = hashes.Hash(hashes.SHA1(), backend=default_backend())
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):  # 4KB
            digest.update(chunk)
    return digest.finalize().hex()


def compare_files(file1, file2):
    hash1 = calculate_sha1(file1)
    hash2 = calculate_sha1(file2)
    print(f"SHA-1 for {file1}: {hash1}")
    print(f"SHA-1 for {file2}: {hash2}")
    if hash1 == hash2:
        print("Collision detected.")
        print("Both files have the same SHA-1 hash.")
    else:
        print("No collision. The SHA-1 hashes are different.")


if __name__ == "__main__":
    file1 = "./files/shattered-1.pdf"
    file2 = "./files/shattered-2.pdf"
    compare_files(file1, file2)

    # https://sha-mbles.github.io/
    # https://shattered.io/