def gf_multiply(a, b, reduc_poly_mod):
    result = 0
    while b > 0:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 0x100:
            a ^= reduc_poly_mod
    return result & 0xFF

a = 57
b = 13
reduc_poly_mod = 0x11B

print(f"Output of {a} * {b} in GF(2^8): {gf_multiply(a, b, reduc_poly_mod)}")
