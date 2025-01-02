from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def sha3_224_hash(message):  # Nie zdążyłem tego zaimplemtnowaować :)
    digest = hashes.Hash(hashes.SHA3_224(), backend=default_backend())
    digest.update(message.encode()) 
    return digest.finalize().hex()   

def driver():
    empty_message = ""
    
    sha3_224_empty = sha3_224_hash(empty_message)
    
    print("SHA3-224 for an empty string:")
    print(f"SHA3-224(\"\"): {sha3_224_empty}")
    
    task_1_result = "6b4e03423667dbb7f8e6e9bba8f9ee90c5a5a5db2c0d0f7c30c7f0d8"
    print("\nComparison with SHA3-224 result from Task 1:")
    print(f"Task 1 SHA3-224 Result: {task_1_result}")
    print(f"Matching Results: {sha3_224_empty == task_1_result}")

if __name__ == "__main__":
    driver()
