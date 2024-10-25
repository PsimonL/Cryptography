import matplotlib.pyplot as plt
import math


def is_coprime(a, b):
    return math.gcd(a, b) == 1


def parity(num):
    return num.bit_count() % 2


def blum_blum_shub(p, q, s):
    n = p * q
    if not is_coprime(s, n):
        raise ValueError("s must be coprime with n = p * q")

    y = []
    z = []

    y_i = (s * s) % n  
    for _ in range(n):
        y.append(y_i)
        z.append(parity(y_i))

        y_i = (y_i * y_i) % n

    plt.title(f"BBS Generator: p={p}, q={q}, s={s}")
    plt.yscale("log")
    plt.plot(y, 'o-', linewidth=0.5, markersize=0.5, color='#FF00FF')
    plt.xlabel("n")
    plt.ylabel("value")
    plt.grid()
    plt.show()

    return ''.join(map(str, z[1:]))


def find_period(stream):
    n = len(stream)
    for period_length in range(1, n // 2 + 1):
        matches = True
        for i in range(n - period_length):
            if stream[i] != stream[i + period_length]:
                matches = False
                break
        if matches:
            return period_length
    return n


tests = [
    (7, 19, 100),   # a) p=7, q=19, s=100
    (67, 71, 100),  # b) p=67, q=71, s=100
    (163, 167, 100) # c) p=163, q=167, s=100
]

for idx, (p, q, s) in enumerate(tests, start=1):
    print(f"\nPrzypadek {idx}: p={p}, q={q}, s={s}")
    try:
        key_stream = list(blum_blum_shub(p, q, s))
        period = find_period(key_stream)
        print(f"Strumień klucza: {''.join(map(str, key_stream[:300]))}")
        print(f"Okres: {period}")
    except ValueError as e:
        print(f"Blad: {e}")
