import numpy as np

# Prawdopodobieństwo tekstu jawnego
prob_P = {'a': 1 / 2, 'b': 1 / 3, 'c': 1 / 6}

def entropy(prob_dist):
    return -sum(p * np.log2(p) for p in prob_dist.values() if p > 0)

H_P = entropy(prob_P)

# Prawdopodobieństwo klucza
prob_K = {'K1': 1 / 3, 'K2': 1 / 3, 'K3': 1 / 3}
H_K = entropy(prob_K)

# Macierz szyfrowania i prawdopodobieństwo szyfrogramu
encryption_matrix = {
    'K1': {'a': 1, 'b': 2, 'c': 3},
    'K2': {'a': 2, 'b': 3, 'c': 4},
    'K3': {'a': 3, 'b': 4, 'c': 1}
}

# Prawdopodobieństwo dla każdego szyfrogramu
prob_C = {1: 0, 2: 0, 3: 0, 4: 0}
for key, mapping in encryption_matrix.items():
    for plaintext, cipher in mapping.items():
        prob_C[cipher] += prob_P[plaintext] * prob_K[key]

H_C = entropy(prob_C)

# H(K|C) = H(K) + H(P) − H(C)
H_K_given_C = H_K + H_P - H_C

# Wzor entropii warunkowej H(P|C)
joint_prob_PC = {}
for key, mapping in encryption_matrix.items():
    for plaintext, cipher in mapping.items():
        joint_prob_PC[(plaintext, cipher)] = prob_P[plaintext] * prob_K[key]

H_PC = -sum(p * np.log2(p) for p in joint_prob_PC.values() if p > 0)
H_P_given_C = H_PC - H_C

print(f"H_P = {H_P}")
print(f"H_C = {H_C}")
print(f"H_K = {H_K}")
print(f"H_K_given_C = {H_K_given_C}")
print(f"H_P_given_C = {H_P_given_C}")
