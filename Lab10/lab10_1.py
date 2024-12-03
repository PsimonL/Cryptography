import numpy as np

A = np.array([
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])

target = np.array([0, 1, 0, 1])

def hash_function(x, A):
    return np.dot(x, A) % 2

solutions = []
for i in range(2**7):
    x = np.array([int(b) for b in format(i, '07b')])
    if np.array_equal(hash_function(x, A), target):
        solutions.append((i, x))

print("Przeciwobrazy:")
for idx, x in solutions:
    print(f"{idx:03d} - {''.join(map(str, x))} - {''.join(map(str, target))}")
