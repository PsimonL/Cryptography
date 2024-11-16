import math

def exact_epsilon(M, Q):
    numerator = math.factorial(M)
    denominator = math.factorial(M - Q) * (M ** Q)
    return 1 - numerator / denominator

def approx_epsilon(M, Q):
    return 1 - math.exp(-Q * (Q - 1) / (2 * M))

M = 365
results = []

for Q in range(15, 31):
    eps = exact_epsilon(M, Q)
    eps_approx = approx_epsilon(M, Q)
    results.append((Q, round(eps, 5), round(eps_approx, 5)))

print(f"{'Q':>3} | {'eps':>7} | {'eps_approx':>10}")
print("-" * 27)
for Q, eps, eps_approx in results:
    print(f"{Q:>3} | {eps:>7.5f} | {eps_approx:>10.5f}")
