sbox = [
    0xE, 0x4, 0xD, 0x1,
    0x2, 0xF, 0xB, 0x8,
    0x3, 0xA, 0x6, 0xC,
    0x5, 0x9, 0x0, 0x7
]


def int_to_bit_string(number, bits=4):
    return ''.join(str((number >> i) & 1) for i in range(bits - 1, -1, -1))


def calculate_difference_distribution_table(sbox):
    difference_table = [[0] * 16 for _ in range(16)]

    for delta_x in range(16):
        for x in range(16):
            x_star = x ^ delta_x
            y = sbox[x]
            y_star = sbox[x_star]

            delta_y = y ^ y_star

            difference_table[delta_x][delta_y] += 1

    return difference_table


difference_table = calculate_difference_distribution_table(sbox)

print("Tabela rozkładu różnic:")
for row in difference_table:
    print(" ".join(f"{val:2d}" for val in row))
