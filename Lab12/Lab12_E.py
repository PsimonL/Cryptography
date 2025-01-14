def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def modular_inverse(a, mod):
    gcd, inverse, _ = gcd_extended(a, mod)
    if gcd != 1:
        raise ValueError(f"Odwrotność modulo nie istnieje dla {a} i {mod}.")
    return inverse % mod


def decrypt_rsa(ciphertexts, n, b):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            break
    else:
        raise ValueError("Nie udało się rozłożyć n na czynniki pierwsze.")

    print(f"n = {n} = {p} * {q}")
    print(f"b = {b}")

    phi = (p - 1) * (q - 1)
    print(f"φ(n) = ({p} - 1) * ({q} - 1) = {phi}")

    a = modular_inverse(b, phi)
    print(f"a = {b}^-1 mod {phi} = {a}\n")

    example_cipher = ciphertexts[0]
    example_plain = pow(example_cipher, a, n)
    print(f"{example_cipher} ^ {a} mod {n} = {example_plain}\n")

    plaintexts = []
    for c in ciphertexts:
        m = pow(c, a, n)
        plaintexts.append(m)

    decoded_text = ""
    for m in plaintexts:
        char1 = m // (26 ** 2)
        char2 = (m % (26 ** 2)) // 26
        char3 = m % 26
        decoded_text += chr(char1 + 65) + chr(char2 + 65) + chr(char3 + 65)

    return decoded_text


n = 18923
b = 1261
ciphertexts = [
    12423, 11524, 7243, 7459, 14303, 6127, 10964, 16399, 9792, 13629, 14407,
    18817, 18830, 13556, 3159, 16647, 5300, 13951, 81, 8986, 8007, 13167,
    10022, 17213, 2264, 961, 17459, 4101, 2999, 14569, 17183, 15827, 12693,
    9553, 18194, 3830, 2664, 13998, 12501, 18873, 12161, 13071, 16900, 7233,
    8270, 17086, 9792, 14266, 13236, 5300, 13951, 8850, 12129, 6091, 18110,
    3332, 15061, 12347, 7817, 7946, 11675, 13924, 13892, 18031, 2620, 6276,
    8500, 201, 8850, 11178, 16477, 10161, 3533, 13842, 7537, 12259, 18110, 44,
    2364, 15570, 3460, 9886, 8687, 4481, 11231, 7547, 11383, 17910, 12867,
    13203, 5102, 4742, 5053, 15407, 2976, 9330, 12192, 56, 2471, 15334, 841,
    13995, 17592, 13297, 2430, 9741, 11675, 424, 6686, 738, 13874, 8168, 7913,
    6246, 14301, 1144, 9056, 15967, 7328, 13203, 796, 195, 9872, 16979, 15404,
    14130, 9105, 2001, 9792, 14251, 1498, 11296, 1105, 4502, 16979, 1105, 56,
    4118, 11302, 5988, 3363, 15827, 6928, 4191, 4277, 10617, 874, 13211, 11821,
    3090, 18110, 44, 2364, 15570, 3460, 9886, 9988, 3798, 1158, 9872, 16979,
    15404, 6127, 9872, 3652, 14838, 7437, 2540, 1367, 2512, 14407, 5053, 1521,
    297, 10935, 17137, 2186, 9433, 13293, 7555, 13618, 13000, 6490, 5310, 18676,
    4782, 11374, 446, 4165, 11634, 3846, 14611, 2364, 6789, 11634, 4493, 4063,
    4576, 17955, 7965, 11748, 14616, 11453, 17666, 925, 56, 4118, 18031, 9522,
    14838, 7437, 3880, 11476, 8305, 5102, 2999, 18628, 14326, 9175, 9061, 650,
    18110, 8720, 15404, 2951, 722, 15334, 841, 15610, 2443, 11056, 2186
]

decoded_message = decrypt_rsa(ciphertexts, n, b)
print("\nOdszyfrowana wiadomość:")
print(decoded_message)
