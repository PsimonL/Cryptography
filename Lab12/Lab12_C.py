from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def chinese_remainder_theorem(moduli, residues):
    M = 1
    for mod in moduli:
        M *= mod
    print(f"Całkowity iloczyn M = {M}\n")

    result = 0
    for i, (mod, res) in enumerate(zip(moduli, residues)):
        Mi = M // mod
        print(f"M{i + 1} = {Mi}")
        _, inverse, _ = gcd_extended(Mi, mod)
        inverse = inverse % mod
        print(f"{Mi}^-1 mod {mod} = {inverse}")
        result += res * Mi * inverse
        print(f"Składnik dla reszty {res}: {res} * {Mi} * {inverse} = {res * Mi * inverse}\n")

    result %= M
    return result


moduli = [3, 5, 7]
residues = [2, 2, 3]
x = chinese_remainder_theorem(moduli, residues)
print(f"χ⁻¹({', '.join(map(str, residues))}) = {x}")
