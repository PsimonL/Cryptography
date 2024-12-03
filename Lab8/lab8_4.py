import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from PIL import Image


def process_image_with_mode(mode_name, mode_instance, key, image_path="Tux.ppm"):
    cipher = Cipher(algorithms.AES(key), mode_instance)
    encryptor = cipher.encryptor()

    with Image.open(image_path) as img:
        image_data = img.tobytes()
        image_size = img.size
        image_mode = img.mode

    padded_data = PKCS7(128).padder().update(image_data) + PKCS7(128).padder().finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_image = Image.frombytes(image_mode, image_size, ciphertext)
    encrypted_image.save(f"Tux_{mode_name}.png")


def encrypt_image_in_modes():
    modes_to_use = {
        "ecb": modes.ECB(),
        "cbc": modes.CBC(os.urandom(16)),
        "ctr": modes.CTR(os.urandom(16)),
    }

    for mode_name, mode_instance in modes_to_use.items():
        key = os.urandom(16)
        process_image_with_mode(mode_name, mode_instance, key)


if __name__ == "__main__":
    encrypt_image_in_modes()
