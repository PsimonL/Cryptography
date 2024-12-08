from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def to_hex(data):
    return data.hex()


key_a = os.urandom(16)
plaintext_a = b'\x00' * 16
cipher_ecb_a = Cipher(algorithms.AES(key_a), modes.ECB(), backend=default_backend())
encryptor_a = cipher_ecb_a.encryptor()
ciphertext_a = encryptor_a.update(plaintext_a) + encryptor_a.finalize()
decryptor_a = cipher_ecb_a.decryptor()
decrypted_a = decryptor_a.update(ciphertext_a) + decryptor_a.finalize()

print("---------- A ----------")
print(f"k = {to_hex(key_a)}")
print(f"enc({to_hex(plaintext_a)}) = {to_hex(ciphertext_a)}")
print(f"dec({to_hex(ciphertext_a)}) = {to_hex(decrypted_a)}\n\n")

key_b = os.urandom(16)
plaintext_b = b'\x00' * 32
cipher_ecb_b = Cipher(algorithms.AES(key_b), modes.ECB(), backend=default_backend())
encryptor_b = cipher_ecb_b.encryptor()
ciphertext_b = encryptor_b.update(plaintext_b) + encryptor_b.finalize()

ciphertext_b1, ciphertext_b2 = ciphertext_b[:16], ciphertext_b[16:]

print("---------- B ----------")
print(f"k = {to_hex(key_b)}")
print(f"enc({to_hex(plaintext_b[:16])} {to_hex(plaintext_b[16:])})")
print(f"=   {to_hex(ciphertext_b1)} {to_hex(ciphertext_b2)}\n\n")

key_c = os.urandom(16)
plaintext_c = b'\x00' * 32

iv_c1 = os.urandom(16)
cipher_cbc_c1 = Cipher(algorithms.AES(key_c), modes.CBC(iv_c1), backend=default_backend())
encryptor_c1 = cipher_cbc_c1.encryptor()
ciphertext_c1 = encryptor_c1.update(plaintext_c) + encryptor_c1.finalize()

iv_c2 = os.urandom(16)
cipher_cbc_c2 = Cipher(algorithms.AES(key_c), modes.CBC(iv_c2), backend=default_backend())
encryptor_c2 = cipher_cbc_c2.encryptor()
ciphertext_c2 = encryptor_c2.update(plaintext_c) + encryptor_c2.finalize()

ciphertext_c1_p1, ciphertext_c1_p2 = ciphertext_c1[:16], ciphertext_c1[16:]
ciphertext_c2_p1, ciphertext_c2_p2 = ciphertext_c2[:16], ciphertext_c2[16:]

print("---------- C ---------")
print(f"k = {to_hex(key_c)}")
print(f"iv ={to_hex(iv_c1)}")
print(f"enc({to_hex(plaintext_c[:16])} {to_hex(plaintext_c[16:])})")
print(f"=   {to_hex(ciphertext_c1_p1)} {to_hex(ciphertext_c1_p2)}")
print()
print(f"iv ={to_hex(iv_c2)}")
print(f"enc({to_hex(plaintext_c[:16])} {to_hex(plaintext_c[16:])})")
print(f"=   {to_hex(ciphertext_c2_p1)} {to_hex(ciphertext_c2_p2)}")
