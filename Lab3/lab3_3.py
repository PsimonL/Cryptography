import matplotlib.pyplot as plt


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a, b):
    return gcd(a, b) == 1


def parity(num):
    return bin(num).count('1') % 2


def blum_blum_shub(p, q, s):
    n = p * q
    if not is_coprime(s, n):
        raise ValueError("s must be coprime with n = p * q.")

    y = []
    z = []

    y_i = (s * s) % n  # y_0
    for _ in range(n):
        y.append(y_i)
        z.append(parity(y_i))

        y_i = (y_i * y_i) % n

    plt.title(f"Generator BBS: p={p}, q={q}, s={s}")
    plt.yscale("log")
    plt.plot(y, 'o-', linewidth=0.5, markersize=1)
    plt.xlabel("Indeks")
    plt.ylabel("Wartość y_i")
    plt.grid()
    plt.show()

    return ''.join(map(str, z[1:]))


def find_period(stream):
    n = len(stream)
    for period_length in range(1, n // 2 + 1):
        if stream[:period_length] == stream[period_length:2 * period_length]:
            return period_length
    return n



test_cases = [
    (7, 19, 100),  # a) p=7, q=19, s=100
    (67, 71, 100),  # b) p=67, q=71, s=100
    (163, 167, 100)  # c) p=163, q=167, s=100
]

for idx, (p, q, s) in enumerate(test_cases, start=1):
    print(f"\nPrzypadek {idx}: p={p}, q={q}, s={s}")
    try:
        key_stream = blum_blum_shub(p, q, s)
        period = find_period(key_stream)
        print(f"Strumień klucza: {key_stream}")
        print(f"Okres: {period}")
    except ValueError as e:
        print(f"Błąd: {e}")

