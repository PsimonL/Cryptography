from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def calculate_md5(file_path):
    digest = hashes.Hash(hashes.MD5(), backend=default_backend())
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):  # 4KB
            digest.update(chunk)
    return digest.finalize().hex()


def compare_files(file1, file2):
    hash1 = calculate_md5(file1)
    hash2 = calculate_md5(file2)
    print(f"MD5 for {file1}:\n{hash1}")
    print(f"MD5 for {file2}:\n{hash2}")
    if hash1 == hash2:
        print("Collision detected.")
        print("Both files have the same MD5 hash.")
    else:
        print("No collision. The MD5 hashes are different.")


if __name__ == "__main__":
    file1 = "./files/letter_of_rec.ps"
    file2 = "./files/order.ps"
    compare_files(file1, file2)
