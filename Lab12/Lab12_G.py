def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result


def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def modular_inverse(a, mod):
    gcd, inverse, _ = gcd_extended(a, mod)
    if gcd != 1:
        raise ValueError(f"Odwrotność modulo nie istnieje dla {a} i {mod}.")
    return inverse % mod


def rsa_decrypt_ctr(p, q, d, y):
    dp = d % (p - 1)
    dq = d % (q - 1)
    print(f"dp = {dp}")
    print(f"dq = {dq}")

    Mp = modular_exponentiation(y, dp, p)
    Mq = modular_exponentiation(y, dq, q)
    print(f"Mp = {Mp}")
    print(f"Mq = {Mq}")

    q_inv = modular_inverse(q, p)
    Xp = (Mp - Mq) * q_inv % p
    print(f"Xp = {Xp}")

    p_inv = modular_inverse(p, q)
    Xq = (Mq - Mp) * p_inv % q
    print(f"Xq = {Xq}")

    x = (Mq + q * Xp) % (p * q)
    print(f"x = {x}")

    return x


p = 1511
q = 2003
d = 1234577
y = 152702

rsa_decrypt_ctr(p, q, d, y)
