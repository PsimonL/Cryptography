class SPN:
    def __init__(self, key, sbox, pbox):
        self.key = key
        self.sbox = sbox
        self.pbox = pbox
        self.k = self.generate_keys()

    def generate_keys(self):
        return [
            0,
            (self.key & 0xFFFF0000) >> 16,
            (self.key & 0x0FFFF000) >> 12,
            (self.key & 0x00FFFF00) >> 8,
            (self.key & 0x000FFFF0) >> 4,
            (self.key & 0x0000FFFF),
        ]

    def encrypt(self, x):
        print(f"Key: {self.key:032b}\n")
        print(f"x : {x:016b}\n")

        w = {0: x}
        print(f"w0: {w[0]:016b}\n")

        N = len(self.k) - 1
        u = {}
        v = {}

        for r in range(1, N):
            print(f"K{r}: {self.k[r]:016b}")
            u[r] = w[r - 1] ^ self.k[r]
            print(f"u{r}: {u[r]:016b}")

            v[r] = self.apply_sbox(u[r])
            print(f"v{r}: {v[r]:016b}")

            w[r] = self.pbox(v[r])
            print(f"w{r}: {w[r]:016b}\n")

        # Final round
        u[N - 1] = w[N - 2] ^ self.k[N - 1]
        v[N - 1] = self.apply_sbox(u[N - 1])

        print(f"K{N}: {self.k[N]:016b}")
        print(f"u{N}: {u[N - 1]:016b}")
        print(f"v{N}: {v[N - 1]:016b}\n")

        # Last key addition
        y = v[N - 1] ^ self.k[N]
        return y

    def apply_sbox(self, u):
        v = 0
        for i in range(4):
            v |= (self.sbox[(u >> (i * 4)) & 0xF] << (i * 4))
        return v


def pbox(v):
    w = 0
    w |= ((v >> 15) & 1) << 15
    w |= ((v >> 11) & 1) << 14
    w |= ((v >> 7) & 1) << 13
    w |= ((v >> 3) & 1) << 12
    w |= ((v >> 14) & 1) << 11
    w |= ((v >> 10) & 1) << 10
    w |= ((v >> 6) & 1) << 9
    w |= ((v >> 2) & 1) << 8
    w |= ((v >> 13) & 1) << 7
    w |= ((v >> 9) & 1) << 6
    w |= ((v >> 5) & 1) << 5
    w |= ((v >> 1) & 1) << 4
    w |= ((v >> 12) & 1) << 3
    w |= ((v >> 8) & 1) << 2
    w |= ((v >> 4) & 1) << 1
    w |= ((v >> 0) & 1) << 0
    return w


def zad1():
    # 0011 1010 1001 0100 1101 0110 0011 1111
    key = 0b00111010100101001101011000111111

    # 0010 0110 1011 0111
    x = 0b0010011010110111

    # Encryption
    sbox = {
        0x0: 0xE,
        0x1: 0x4,
        0x2: 0xD,
        0x3: 0x1,
        0x4: 0x2,
        0x5: 0xF,
        0x6: 0xB,
        0x7: 0x8,
        0x8: 0x3,
        0x9: 0xA,
        0xA: 0x6,
        0xB: 0xC,
        0xC: 0x5,
        0xD: 0x9,
        0xE: 0x0,
        0xF: 0x7
    }

    spn_cipher = SPN(key, sbox, pbox)
    y = spn_cipher.encrypt(x)
    print(f"y : {y:016b}\n\n")


def main():
    zad1()


if __name__ == '__main__':
    main()
