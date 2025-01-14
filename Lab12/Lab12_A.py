from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


a, b = 57, 93
gcd, s, t = gcd_extended(a, b)
print(f"NWD({a}, {b}) = {gcd}, s = {s}, t = {t}, 57s + 93t = {57 * s + 93 * t}")