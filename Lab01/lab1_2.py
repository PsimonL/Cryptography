"""
Zaimplementuj obliczanie odwrotności multiplikatywnej a) z definicji – metodą prób i
błędów, b) za pomocą rozszerzonego algorytmu Euklidesa. Wypisz odwrotności 1, 3, 5, 7, 9, 11, 15,
17, 19, 21, 23, 25 w Z26.
"""
def multiplicative_inverse_trial_and_error(x: int, mod: int) -> int:
    """
    Finds the multiplicative inverse of x modulo mod using a trial-and-error method.
    This function iterates through possible values of y from 1 to mod-1
    and checks if the product of x and y is congruent to 1 modulo mod.
    Parameters:
    x (int): The integer for which the multiplicative inverse is to be found.
    mod (int): The modulus to be used in the calculation.
    Returns:
    int: The multiplicative inverse of x modulo mod, or None if it does not exist.
    """
    for y in range(1, mod):
        if (x * y) % mod == 1:
            return y
    return None


def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def multiplicative_inverse_extended_euclidean(x, mod):
    gcd, inv, _ = extended_euclidean(x, mod)
    if gcd != 1:
        return None
    return inv % mod


Z26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
mod = 26

inverses_trial_and_error = {x: multiplicative_inverse_trial_and_error(x, mod) for x in Z26}
inverses_extended_euclidean = {x: multiplicative_inverse_extended_euclidean(x, mod) for x in Z26}

print("Inversions with method trial and error - Z26:")
for x, inv in inverses_trial_and_error.items():
    print(f"inf of {x} is {inv}")

print()

print("Inversions with Extended Euclidean algorithm - Z26:")
for x, inv in inverses_extended_euclidean.items():
    print(f"GCD_ext: inf of {x} is {inv}")

"""
Inversions with method trial and error - Z26:
inf of 1 is 1
inf of 3 is 9
inf of 5 is 21
inf of 7 is 15
inf of 9 is 3
inf of 11 is 19
inf of 15 is 7
inf of 17 is 23
inf of 19 is 11
inf of 21 is 5
inf of 23 is 17
inf of 25 is 25

Inversions with Extended Euclidean algorithm - Z26:
GCD_ext: inf of 1 is 1
GCD_ext: inf of 3 is 9
GCD_ext: inf of 5 is 21
GCD_ext: inf of 7 is 15
GCD_ext: inf of 9 is 3
GCD_ext: inf of 11 is 19
GCD_ext: inf of 15 is 7
GCD_ext: inf of 17 is 23
GCD_ext: inf of 19 is 11
GCD_ext: inf of 21 is 5
GCD_ext: inf of 23 is 17
GCD_ext: inf of 25 is 25
"""
