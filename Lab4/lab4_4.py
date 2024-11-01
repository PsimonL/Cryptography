import numpy as np

def entropy(prob_dist):
    """Entropia na podstawie rozkładu prawdopodobieństwa"""
    return -sum(p * np.log2(p) for p in prob_dist if p > 0)

# Uczciwy
prob_honest = np.array([1/2, 1/2])
H_honest = entropy(prob_honest)

# Nieuważny; P(reszka) = 1/4, P(orzeł) = 3/4
prob_unfair_1 = np.array([3/4, 1/4])
H_unfair_1 = entropy(prob_unfair_1)

# P(reszka) = 1/100, P(orzeł) = 99/100
prob_unfair_2 = np.array([99/100, 1/100])
H_unfair_2 = entropy(prob_unfair_2)

print(f"Entropia uczciwego rzutu monetą: {H_honest:.4f} bitów")
print(f"Entropia dla P(reszka) = 1/4: {H_unfair_1:.4f} bitów")
print(f"Entropia dla P(reszka) = 1/100: {H_unfair_2:.4f} bitów")
