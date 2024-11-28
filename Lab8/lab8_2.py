from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def increment_iv(iv):
    iv_int = int.from_bytes(iv, byteorder='big') + 1
    return iv_int.to_bytes(len(iv), byteorder='big')


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def format_bytes_as_hex(byte_data):
    return byte_data.hex()


def ctr_encrypt(message, key):
    iv = b'\x00' * 16
    encrypted_message = b''

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    for i in range(0, len(message), 16):
        encrypted_iv = encryptor.update(iv)

        chunk = message[i:i + 16]
        encrypted_chunk = xor_bytes(encrypted_iv, chunk)
        encrypted_message += encrypted_chunk

        iv = increment_iv(iv)

    return encrypted_message


key = os.urandom(16)

plain_text = "0101010101010101010101010101010101010101010101010101010101010101"
plain_text_bytes = bytes.fromhex("0101010101010101010101010101010101010101010101010101010101010101")

ciphertext = ctr_encrypt(plain_text_bytes, key)

print(f"k = {format_bytes_as_hex(key)}")
iv_hex = '00' * 16
print(f"iv = {iv_hex}")

print(
    f"CTR: enc({plain_text[:32]} {plain_text[32:]}) = {format_bytes_as_hex(ciphertext)}")

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
encryptor = cipher.encryptor()

iv_0 = b'\x00' * 16
iv_1 = increment_iv(iv_0)

encrypted_iv_0 = encryptor.update(iv_0)
encrypted_iv_1 = encryptor.update(iv_1)

ecb_enc_output = f"{format_bytes_as_hex(encrypted_iv_0)} {format_bytes_as_hex(encrypted_iv_1)}"

xor_result = b''
iv = iv_0
for i in range(0, len(plain_text_bytes), 16):
    encrypted_iv = encryptor.update(iv)
    chunk = plain_text_bytes[i:i + 16]
    xor_result += xor_bytes(encrypted_iv, chunk)
    iv = increment_iv(iv)

print()
print(f"ECB: enc({format_bytes_as_hex(iv_0)} {format_bytes_as_hex(iv_1)}) = {ecb_enc_output}")
print(f"plain_text = {format_bytes_as_hex(plain_text_bytes)[:32]} {format_bytes_as_hex(plain_text_bytes)[32:]}")
print(f"XOR(ECB_enc, plain_text) = {format_bytes_as_hex(xor_result)[:32]} {format_bytes_as_hex(xor_result)[32:]}")
