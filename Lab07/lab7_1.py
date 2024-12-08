sbox = {
    0x0: 0xE, 0x1: 0x4, 0x2: 0xD, 0x3: 0x1,
    0x4: 0x2, 0x5: 0xF, 0x6: 0xB, 0x7: 0x8,
    0x8: 0x3, 0x9: 0xA, 0xA: 0x6, 0xB: 0xC,
    0xC: 0x5, 0xD: 0x9, 0xE: 0x0, 0xF: 0x7
}

def int_to_bit_string(number, bits=4):
    return ''.join(str((number >> i) & 1) for i in range(bits-1, -1, -1))

x_prime = 0xB
x_values = list(range(16))
x_star = [x ^ x_prime for x in x_values]

y = [sbox[x] for x in x_values]
y_star = [sbox[xs] for xs in x_star]
y_prime = [y[i] ^ y_star[i] for i in range(16)]

xor_counts = [0] * 16
for yp in y_prime:
    xor_counts[yp] += 1

print("      x |   x* |    y |   y* |   y'")
for i in range(16):
    print(f"{i:01X}: {int_to_bit_string(x_values[i])} | {int_to_bit_string(x_star[i])} | "
          f"{int_to_bit_string(y[i])} | {int_to_bit_string(y_star[i])} | {int_to_bit_string(y_prime[i])}")

print("\nXOR Counts:")
for i in range(16):
    print(f"{int_to_bit_string(i)} ", end='')
print()
for count in xor_counts:
    print(f"{count:4}", end=' ')
print()
