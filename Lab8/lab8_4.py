from Crypto.Hash import MD4

def calculate_md4(hex_string):
    h = MD4.new()
    h.update(bytes.fromhex(hex_string))
    return h.hexdigest()

messages = {
    "m1": "839c7a4d7a92cb5678a5d5b9eea5a7573c8a74deb366c3dc20a083b69f5d2a3bb3719dc69891e9f95e809fd7e8b23ba6318edd45e51fe39708bf9427e9c3e8b9",
    "m2": "839c7a4d7a92cbd678a5d529eea5a7573c8a74deb366c3dc20a083b69f5d2a3bb3719dc69891e9f95e809fd7e8b23ba6318edc45e51fe39708bf9427e9c3e8b9",
    "m3": "a6af943ce36f0cf4adcb12bef7f0dc1f526dd914bd3da3cafde14467ab129e640b4c41819915cb43db752155ae4b895fc71b9b0d384d06ef3118bbc643ae6384",
    "m4": "a6af943ce36f0c74adcb122ef7f0dc1f526dd914bd3da3cafde14467ab129e640b4c41819915cb43db752155ae4b895fc71b9a0d384d06ef3118bbc643ae6384",
    "m5": "76931fac9dab2b36c248b87d6ae33f9a62d7183a5d5789e4b2d6b441e2411dc709e111c7e1e7acb6f8cac0bb2fc4c8bc2ae3baaab9165cc458e199cb89f51b13",
    "m6": "76931fac9dab2b36d248b87d6af33f9a62d7183a5d5789e4b2d6b441e2411dc709e111c7e1e7acb6f8cac0bb2fc4c8bc2ae3baaab9265cc458e199cb89f51b13",
}

pairs = [("m1", "m2"), ("m3", "m4"), ("m5", "m6")]
for m1, m2 in pairs:
    hash1 = calculate_md4(messages[m1])
    hash2 = calculate_md4(messages[m2])
    print(f"{m1} vs {m2}:")
    print(f"  Hash {m1}: {hash1}")
    print(f"  Hash {m2}: {hash2}")
    print(f"  Kolizja: {'TAK' if hash1 == hash2 else 'NIE'}\n")
