from cryptography.hazmat.primitives import padding

def pad_data(data, block_size=16):
    padder = padding.PKCS7(block_size * 8).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def unpad_data(padded_data, block_size=16):
    unpadder = padding.PKCS7(block_size * 8).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

samples = [
    b'!!!!!!!!!!!!!!!',
    b'!!!!!!!!!!!!!!!',
    b'!!!!!!!!',
    b''
]

for data in samples:
    padded_data = pad_data(data)
    unpadded_data = unpad_data(padded_data)

    print(f"data = {data}")
    print(f"padded_data = {padded_data}")
    print(f"UNpadded_data = {unpadded_data}")
    print()

 # :)