from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

for num, mod in [(17, 101), (357, 1234), (3125, 9987)]:
    gcd, inv, _ = gcd_extended(num, mod)
    if gcd != 1:
        print(f"Nie istnieje odwrotność multiplikatywna dla {num} mod {mod}")
    else:
        print(f"Odwrotność multiplikatywna {num}^-1 mod {mod} = {inv % mod}")