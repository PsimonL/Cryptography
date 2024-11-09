def print_bits(number, num_bits=4):
    """Prints the binary representation of a number."""
    bits = [(number >> i) & 1 for i in range(num_bits - 1, -1, -1)]
    print(" ".join(map(str, bits)), end=" ")


def generate_key(key):
    """Generates the list of 4-bit keys from the given binary key."""
    return [(key >> (i * 4)) & 0xF for i in range(7, -1, -1)]


def sbox_lookup(value, S_Box):
    """Looks up a value in the S-Box."""
    return S_Box[value]


def apply_permutation(bits, P_Box):
    """Applies the permutation defined by P_Box to the input bits."""
    return [bits[P_Box[j] - 1] for j in range(len(P_Box))]


def calculate_u(w, key, r, l):
    """Calculates u values using w and the key."""
    return [w[j] ^ key[j + r] for j in range(l)]


def calculate_v(u, S_Box):
    """Calculates v values using u and S-Box."""
    return [sbox_lookup(u[i], S_Box) for i in range(len(u))]


def update_w(v, P_Box, m):
    """Updates w values based on v and the P-Box."""
    all_bits = []

    for j in range(m):
        bits = [(v[j] >> i) & 1 for i in range(4)]
        all_bits.extend(reversed(bits))

    permuted_bits = apply_permutation(all_bits, P_Box)

    w = []
    for j in range(4):
        result = 0
        for i in range(4):
            result = (result << 1) | permuted_bits[j * 4 + i]
        w.append(result)

    return w


def spn_algorithm():
    Key = 0b00111010100101001101011000111111
    Key = generate_key(Key)

    # Define x in binary format
    x = 0b0010011010110111  # equivalent to [2, 6, 11, 7]
    w = [0x2, 0x6, 0xB, 0x7]  # Initial w values

    m = 4  # Number of bits in each block
    N = 4  # Number of rounds

    # S-Box and P-Box
    S_Box = [0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7]
    P_Box = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
    l = 4  # Length of the key used in each round

    for r in range(N - 1):
        print(f"\nK{r + 1}: ", end="")
        for j in range(l):
            print_bits(Key[j + r])

        u = calculate_u(w, Key, r, l)
        print(f"\nu{r + 1}: ", end="")
        for j in range(l):
            print_bits(u[j])

        v = calculate_v(u, S_Box)
        print(f"\nv{r + 1}: ", end="")
        for i in range(m):
            print_bits(v[i])

        print(f"\nw{r + 1}: ", end="")
        w = update_w(v, P_Box, m)
        for j in range(4):
            print_bits(w[j])

    print(f"\nK{N}: ", end="")
    for j in range(l):
        print_bits(Key[j + N - 1])

    u = calculate_u(w, Key, N - 1, l)
    print(f"\nu{N}: ", end="")
    for j in range(l):
        print_bits(u[j])

    v = calculate_v(u, S_Box)
    print(f"\nv{N}: ", end="")
    for i in range(m):
        print_bits(v[i])

    print(f"\n\nK{N + 1}: ", end="")
    for j in range(l):
        print_bits(Key[j + N])

    print(f"\n\ny: ", end="")
    y = [v[j] ^ Key[j + N] for j in range(l)]
    for j in range(l):
        print_bits(y[j])


if __name__ == "__main__":
    # Encryption
    spn_algorithm()
    # TODO: Decription
