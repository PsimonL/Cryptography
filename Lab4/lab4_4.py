

"""
Dla kluczy o długości nn bitów, przy jednorodnym (równomiernym) rozkładzie, entropia będzie maksymalna.
Entropia H(X) liczona jest jako:
H(X)=−i∑P(xi)log2(P(xi))
W przypadku kluczy o nn bitach mamy 2^n możliwych wartości, a przy jednorodnym rozkładzie każde xi ma prawdopodobieństwo:
P(xi):
P(xi)=1/2^n

Wstawiając to do wzoru na entropię, otrzymujemy:
H(X)=−∑1/2^n * log2(1/2^n)=−2n * 1/2^n * (−n)=n bitow
"""

def entropy_uniform_keys(n):
    return n

entropy_128 = entropy_uniform_keys(128)
print(f"Entropia 128-bitowego klucza: {entropy_128} bitów")

n = 256
entropy_n = entropy_uniform_keys(n)
print(f"Entropia {n}-bitowego klucza: {entropy_n} bitów")
