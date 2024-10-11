def multiplicative_inverse_trial_and_error(x, mod):
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

print("Inversions with Extended Euclidean algorithm - Z26:")
for x, inv in inverses_extended_euclidean.items():
    print(f"GCD_ext: inf of {x} is {inv}")
