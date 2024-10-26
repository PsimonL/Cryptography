def print_bits(number):
    num_bits = 4
    bits = []
    for i in range(num_bits - 1, -1, -1):
        bit = (number >> i) & 1
        bits.append(str(bit))
    print(" ".join(bits), end=" ")


def main():
    Key = [0x3, 0xA, 0x9, 0x4, 0xD, 0x6, 0x3, 0xF]
    x = [2, 6, 11, 7]
    w = [0x2, 0x6, 0xB, 0x7]

    m = 4
    u = [0] * m
    v = [0] * m
    N = 4
    PI_S = [0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7]
    PI_P = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
    l = 4

    for r in range(N - 1):
        print(f"\nK{r + 1}: ", end="")
        for j in range(l):
            print_bits(Key[j + r])

        print(f"\nu{r + 1}: ", end="")
        for j in range(l):
            u[j] = w[j] ^ Key[j + r]
            print_bits(u[j])

        print(f"\nv{r + 1}: ", end="")
        for i in range(m):
            v[i] = PI_S[u[i]]
            print_bits(v[i])

        all_bits = [0] * 16

        print(f"\nw{r + 1}: ", end="")
        for j in range(m):
            bits = [(v[j] >> i) & 1 for i in range(4)]
            reversed_bits = bits[::-1]

            for i in range(len(reversed_bits)):
                all_bits[j * 4 + i] = reversed_bits[i]

        all_bits2 = [0] * 16
        for j in range(16):
            all_bits2[j] = all_bits[PI_P[j] - 1]

        for j in range(4):
            result = 0
            for i in range(4):
                result = (result << 1) | all_bits2[j * 4 + i]
            w[j] = result
            print_bits(w[j])

        print()

    print(f"\nK{N}: ", end="")
    for j in range(l):
        print_bits(Key[j + N - 1])

    print(f"\nu{N}: ", end="")
    for j in range(l):
        u[j] = w[j] ^ Key[j + N - 1]
        print_bits(u[j])

    print(f"\nv{N}: ", end="")
    for i in range(m):
        v[i] = PI_S[u[i]]
        print_bits(v[i])

    print(f"\n\nK{N + 1}: ", end="")
    for j in range(l):
        print_bits(Key[j + N])

    print(f"\n\ny: ", end="")
    y = [0] * 4
    for j in range(l):
        y[j] = v[j] ^ Key[j + N]
        print_bits(y[j])


if __name__ == "__main__":
    main()
