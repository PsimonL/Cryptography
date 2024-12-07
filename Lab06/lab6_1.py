x1 = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]]
x2 = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]]
x3 = [[0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]]
x4 = [[0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]]

y1 = [[1, 0, 1, 0], [0, 1, 1, 1], [0, 1, 0, 1], [0, 1, 0, 0]]
y2 = [[1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1]]
y3 = [[1, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1]]
y4 = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 0], [1, 1, 0, 1]]


def calculate_xor_and_eps(a, b, c, d=None):
    count0 = 0
    count1 = 0
    xor_result = ""

    for i in range(4):
        for j in range(4):
            result = a[i][j] ^ b[i][j] ^ c[i][j]
            if d is not None:
                result ^= d[i][j]

            if result == 0:
                count0 += 1
                xor_result += "0"
            else:
                count1 += 1
                xor_result += "1"
        xor_result += " "

    Pr_0 = count0 / 16.0
    Pr_1 = count1 / 16.0
    Ep_0 = (count0 - 8.0) / 16.0
    Ep_1 = (count1 - 8.0) / 16.0

    return xor_result, Pr_0, Pr_1, Ep_0, Ep_1


# X1 ⊕ X4 ⊕ Y2
xor_result_1, Pr_0_1, Pr_1_1, Ep_0_1, Ep_1_1 = calculate_xor_and_eps(x1, x4, y2)
print(f"X1 ⊕ X4 ⊕ Y2 = {xor_result_1}")
print(f"Pr[X1 ⊕ X4 ⊕ Y2 = 0] = {Pr_0_1}")
print(f"Pr[X1 ⊕ X4 ⊕ Y2 = 1] = {Pr_1_1}")
print(f"eps[X1 ⊕ X4 ⊕ Y2 = 0] = {Ep_0_1}")
print(f"eps[X1 ⊕ X4 ⊕ Y2 = 1] = {Ep_1_1}")

# X3 ⊕ X4 ⊕ Y1 ⊕ Y4
xor_result_2, Pr_0_2, Pr_1_2, Ep_0_2, Ep_1_2 = calculate_xor_and_eps(x3, x4, y1, y4)
print(f"\nX3 ⊕ X4 ⊕ Y1 ⊕ Y4 = {xor_result_2}")
print(f"Pr[X3 ⊕ X4 ⊕ Y1 ⊕ Y4 = 0] = {Pr_0_2}")
print(f"Pr[X3 ⊕ X4 ⊕ Y1 ⊕ Y4 = 1] = {Pr_1_2}")
print(f"eps[X3 ⊕ X4 ⊕ Y1 ⊕ Y4 = 0] = {Ep_0_2}")
print(f"eps[X3 ⊕ X4 ⊕ Y1 ⊕ Y4 = 1] = {Ep_1_2}")
