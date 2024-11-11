import numpy as np

# Definicje macierzy wejściowych X i wyjściowych Y
x1 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]])
x2 = np.array([[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]])
x3 = np.array([[0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]])
x4 = np.array([[0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]])

y1 = np.array([[1, 0, 1, 0], [0, 1, 1, 1], [0, 1, 0, 1], [0, 1, 0, 0]])
y2 = np.array([[1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1]])
y3 = np.array([[1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1]])
y4 = np.array([[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 0, 1]])

# Przechowujemy macierze wejściowe i wyjściowe w listach
X = [x1, x2, x3, x4]
Y = [y1, y2, y3, y4]

# Inicjalizacja tabeli NL (Licznik wartości XOR równych 0 dla każdej pary kombinacji A i B)
NL = np.zeros((16, 16), dtype=int)

# Funkcja konwersji liczby całkowitej na 4-bitową tablicę bitową
def int_to_bit_array(number):
    return [(number >> i) & 1 for i in range(3, -1, -1)]

# Obliczanie tabeli NL
for l in range(16):
    B = int_to_bit_array(l)
    for k in range(16):
        A = int_to_bit_array(k)
        count = 0
        for i in range(4):
            for j in range(4):
                # Obliczanie wartości XOR dla danej kombinacji A i B
                x_val = sum(A[m] * X[m][i][j] for m in range(4)) % 2
                y_val = sum(B[m] * Y[m][i][j] for m in range(4)) % 2
                if x_val == y_val:
                    count += 1
        NL[l][k] = count

# Wypisywanie tabeli NL
print("Tabela NL:")
for row in NL:
    print(" ".join(f"{val:2d}" for val in row))

# Obliczanie odchylenia Ep (NL - 8) / 16
Ep = (NL - 8) / 16.0

# Wypisywanie tabeli Ep
print("\nTabela Ep:")
for row in Ep:
    print(" ".join(f"{val:+.3f}" for val in row))
