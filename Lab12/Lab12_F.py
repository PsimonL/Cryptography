def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result


def diffie_hellman(p, g, a, b):
    A = modular_exponentiation(g, a, p)
    print(f"Alicja oblicza:\nA = g^a mod p = {g}^{a} mod {p} = {A}")

    B = modular_exponentiation(g, b, p)
    print(f"Bob oblicza:\nB = g^b mod p = {g}^{b} mod {p} = {B}")

    K_A = modular_exponentiation(B, a, p)
    print(f"Alicja oblicza klucz:\nK_A = B^a mod p = {B}^{a} mod {p} = {K_A}")

    K_B = modular_exponentiation(A, b, p)
    print(f"Bob oblicza klucz:\nK_B = A^b mod p = {A}^{b} mod {p} = {K_B}")

    if K_A == K_B:
        print(f"Wspólny klucz to K = {K_A}")
    else:
        print("Błąd: klucze się nie zgadzają. Cos jest nie tak!")
    return K_A, K_B


p = 12987461
g = 3606738
a = 357
b = 199

diffie_hellman(p, g, a, b)
