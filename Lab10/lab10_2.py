import math


def exact_epsilon(M, Q):
    numerator = math.factorial(M)
    denominator = math.factorial(M - Q) * (M ** Q)
    return 1 - numerator / denominator


def approx_epsilon(M, Q):
    return 1 - math.exp(-Q * (Q - 1) / (2 * M))


M = 365
results = []

ranges = [(20, 31), (50, 61)]

for each in ranges:
    print(each)
    for Q in range(each[0], each[1]):
        eps = exact_epsilon(M, Q)
        eps_approx = approx_epsilon(M, Q)
        results.append((Q, round(eps, 5), round(eps_approx, 5)))

    print(f"{'Q':>3} | {'eps':>7} | {'eps_approx':>10}")
    print("-" * 27)
    for Q, eps, eps_approx in results:
        print(f"{Q:>3} | {eps:>7.5f} | {eps_approx:>10.5f}")

    print()
    eps, eps_approx, Q = 0, 0, 0
    results.clear()

# Z tabeli wyników dla zakresu Q∈[20,31], widocznym jest, że ε przekracza 0.5 po raz pierwszy dla Q=23, gdzie ε=0.50730.
# Zatem liczba osób w grupie musi wynosić co najmniej 23, aby prawdopodobieństwo wynosiło co najmniej 0.5.

# Z tabeli wyników dla zakresu Q∈[50,61], widocznym jest, że ε przekracza 0.990 po raz pierwszy dla Q=57, gdzie ε=0.99012.
# Zatem liczba osób w grupie musi wynosić co najmniej 57, aby prawdopodobieństwo wynosiło co najmniej 0.990.