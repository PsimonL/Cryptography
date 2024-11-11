import random


def print_bits(number, num_bits=4):
    bits = [(number >> i) & 1 for i in range(num_bits - 1, -1, -1)]
    print(" ".join(map(str, bits)), end=" ")


def generate_key(key):
    return [(key >> (i * 4)) & 0xF for i in range(7, -1, -1)]


def sbox_lookup(value, S_Box):
    return S_Box[value]


def apply_permutation(bits, P_Box):
    return [bits[P_Box[j] - 1] for j in range(len(P_Box))]


def calculate_u(w, key, r, l):
    return [w[j] ^ key[j + r] for j in range(l)]


def calculate_v(u, S_Box):
    return [sbox_lookup(u[i], S_Box) for i in range(len(u))]


def update_w(v, P_Box, m):
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


def spn_algorithm(Key_, x):
    Key = Key_[:]
    w = x[:]
    m = 4
    N = 4
    S_Box = [0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7]
    P_Box = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
    l = 4

    for r in range(N - 1):
        u = calculate_u(w, Key, r, l)
        v = calculate_v(u, S_Box)
        w = update_w(v, P_Box, m)

    u = calculate_u(w, Key, N - 1, l)
    v = calculate_v(u, S_Box)
    y = [v[j] ^ Key[j + N] for j in range(l)]
    return y


def bit_array_to_int(bit_array):
    result = 0
    for bit in bit_array:
        result = (result << 1) | bit
    return result


def int_to_bit_array(number):
    bit_array = [0] * 4
    for i in range(3, -1, -1):
        bit_array[i] = number & 1
        number >>= 1
    return bit_array


def generate_input_data(num_samples=8000):
    Key = [0x3, 0xA, 0x9, 0x4, 0xD, 0x6, 0x3, 0xF]
    x = [[[0] * 4 for _ in range(4)] for _ in range(num_samples)]
    y = [[0] * 4 for _ in range(num_samples)]

    for i in range(num_samples):
        xTmpTab = [0] * 4
        for j in range(4):
            xTmp = (random.randint(0, 15) + 16) % 16
            x[i][j] = int_to_bit_array(xTmp)
            xTmpTab[j] = xTmp
        y[i] = spn_algorithm(Key, xTmpTab)

    return x, y, Key


def linear_attack(x, y, num_samples=8000):
    S_Box_Inverse = [0xE, 3, 4, 8, 1, 0xC, 0xA, 0xF, 7, 0xD, 9, 6, 0xB, 2, 0, 5]
    count = [[0] * 16 for _ in range(16)]

    for r in range(num_samples):
        for l in range(16):
            L1 = int_to_bit_array(l)
            for k in range(16):
                L2 = int_to_bit_array(k)

                y_temp_1 = int_to_bit_array(y[r][1])
                y_temp_3 = int_to_bit_array(y[r][3])

                v2 = [L1[j] ^ y_temp_1[j] for j in range(4)]
                v4 = [L2[j] ^ y_temp_3[j] for j in range(4)]

                v2_int = bit_array_to_int(v2)
                v4_int = bit_array_to_int(v4)
                u2_int = S_Box_Inverse[v2_int]
                u4_int = S_Box_Inverse[v4_int]

                u2_bits = int_to_bit_array(u2_int)
                u4_bits = int_to_bit_array(u4_int)

                z = (x[r][1][0] ^ x[r][1][2]) ^ (x[r][1][3] ^ u2_bits[1]) ^ u2_bits[3] ^ u4_bits[1] ^ u4_bits[3]
                if z == 0:
                    count[l][k] += 1

    max_count, maxL1, maxL2 = -1, 0, 0
    for i in range(16):
        for j in range(16):
            count[i][j] = abs(count[i][j] - num_samples // 2)
            if count[i][j] > max_count:
                max_count, maxL1, maxL2 = count[i][j], i, j

    return max_count, maxL1, maxL2


def display_results(maxL1, maxL2):
    tmp = int_to_bit_array(maxL1)
    tmp2 = int_to_bit_array(maxL2)
    print("Key: xxxx " + "".join(map(str, tmp)) + " xxxx " + "".join(map(str, tmp2)))


def runner():
    num_samples = 10000
    x, y, Key = generate_input_data(num_samples)
    max_count, maxL1, maxL2 = linear_attack(x, y, num_samples)
    display_results(maxL1, maxL2)


if __name__ == "__main__":
    runner()
