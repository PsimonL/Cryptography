import struct


def sha1(data: bytes) -> str:
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    original_bit_length = len(data) * 8
    data += b'\x80'
    while (len(data) * 8) % 512 != 448:
        data += b'\x00'
    data += struct.pack('>Q', original_bit_length)

    for chunk_start in range(0, len(data), 64):
        chunk = data[chunk_start:chunk_start + 64]
        w = list(struct.unpack('>16L', chunk))
        for i in range(16, 80):
            word = (w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16])
            w.append((word << 1 | word >> 31) & 0xFFFFFFFF)

        a, b, c, d, e = h0, h1, h2, h3, h4

        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = ((a << 5 | a >> 27) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = (b << 30 | b >> 2) & 0xFFFFFFFF
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    return ''.join(f'{x:08x}' for x in (h0, h1, h2, h3, h4))


def sha1_format(data: bytes) -> str:
    raw_hash = sha1(data)
    formatted = ' '.join(raw_hash[i:i + 2].upper() for i in range(0, len(raw_hash), 2))
    return formatted


def printer(formatted, data):
    print(f"Test for {data}:")
    print(formatted)


if __name__ == "__main__":
    printer(sha1_format(b"a"), "a")
    printer(sha1_format(b"b"), "b")
    printer(sha1_format(b"c"), "c")
    printer(sha1_format(b"abc"), "abc")

    # https://10015.io/tools/sha1-encrypt-decrypt
