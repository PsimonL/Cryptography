# Tabela podstawień S-Box
sbox = [
    0xE, 0x4, 0xD, 0x1,
    0x2, 0xF, 0xB, 0x8,
    0x3, 0xA, 0x6, 0xC,
    0x5, 0x9, 0x0, 0x7
]


# Funkcja do konwersji liczby na postać bitową
def int_to_bit_string(number, bits=4):
    return ''.join(str((number >> i) & 1) for i in range(bits - 1, -1, -1))


# Obliczanie tabeli rozkładu różnic
def calculate_difference_distribution_table(sbox):
    # Inicjalizacja tabeli różnic 16x16
    difference_table = [[0] * 16 for _ in range(16)]

    # Iteracja po wszystkich możliwych wartościach różnic wejściowych (delta_x)
    for delta_x in range(16):
        for x in range(16):
            # Obliczanie y oraz y* dla każdej wartości x
            x_star = x ^ delta_x
            y = sbox[x]
            y_star = sbox[x_star]

            # Obliczenie różnicy wyjściowej (delta_y)
            delta_y = y ^ y_star

            # Zwiększenie licznika w tabeli dla uzyskanej różnicy delta_y
            difference_table[delta_x][delta_y] += 1

    return difference_table


# Generowanie tabeli różnic
difference_table = calculate_difference_distribution_table(sbox)

# Wyświetlenie tabeli różnic
print("Tabela rozkładu różnic:")
for row in difference_table:
    print(" ".join(f"{val:2d}" for val in row))
