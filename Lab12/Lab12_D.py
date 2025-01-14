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


def solve_congruences():
    print("13x = 4 (mod 99)")
    print("15x = 56 (mod 101)\n")

    mod1 = 99
    a1 = 13
    b1 = 4
    inverse1 = modular_inverse(a1, mod1)
    print(f"13^-1 mod 99 = {inverse1}")
    x1 = (b1 * inverse1) % mod1
    print(f"x = {x1} (mod {mod1})\n")

    mod2 = 101
    a2 = 15
    b2 = 56
    inverse2 = modular_inverse(a2, mod2)
    print(f"15^-1 mod 101 = {inverse2}")
    x2 = (b2 * inverse2) % mod2
    print(f"x = {x2} (mod {mod2})\n")

    moduli = [mod1, mod2]
    residues = [x1, x2]
    M = 1
    for mod in moduli:
        M *= mod

    result = 0
    for mod, res in zip(moduli, residues):
        Mi = M // mod
        inverse = modular_inverse(Mi, mod)
        result += res * Mi * inverse

    result %= M
    print(f"x = {result}")


solve_congruences()
