

# Przypuśćmy, że mamy następujący klucz 128-bitowy AES, podany w notacji
# heksadecymalnej:
# Cipher Key = 2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c
# Korzystając z algorytmu przedstawionego na wykładzie, skonstruuj kompletny harmonogram
# kluczy wynikający z tego klucza.




# from typing import List
#
# S_BOX = {
#     0x0: 0xE, 0x1: 0x4, 0x2: 0xD, 0x3: 0x1,
#     0x4: 0x2, 0x5: 0xF, 0x6: 0xB, 0x7: 0x8,
#     0x8: 0x3, 0x9: 0xA, 0xA: 0x6, 0xB: 0xC,
#     0xC: 0x5, 0xD: 0x9, 0xE: 0x0, 0xF: 0x7
# }
#
# RCON = [
#     [0x01, 0x00, 0x00, 0x00],
#     [0x02, 0x00, 0x00, 0x00],
#     [0x04, 0x00, 0x00, 0x00],
#     [0x08, 0x00, 0x00, 0x00],
#     [0x10, 0x00, 0x00, 0x00],
#     [0x20, 0x00, 0x00, 0x00],
#     [0x40, 0x00, 0x00, 0x00],
#     [0x80, 0x00, 0x00, 0x00],
#     [0x1b, 0x00, 0x00, 0x00],
#     [0x36, 0x00, 0x00, 0x00],
# ]
#
# def sbox_lookup(byte: int) -> int:
#     return S_BOX[byte >> 4] << 4 | S_BOX[byte & 0xF]
#
# def sub_word(word: List[int]) -> List[int]:
#     return [sbox_lookup(byte) for byte in word]
#
# def rot_word(word: List[int]) -> List[int]:
#     return word[1:] + word[:1]
#
# def key_expansion(cipher_key: List[int]) -> List[List[int]]:
#     assert len(cipher_key) == 16, "Cipher key must be 128 bits (16 bytes)."
#
#     words = [cipher_key[i:i + 4] for i in range(0, len(cipher_key), 4)]
#
#     for i in range(4, 44):
#         temp = words[i - 1]
#         if i % 4 == 0:
#             temp = sub_word(rot_word(temp))  # Apply SubWord and RotWord
#             temp = [t ^ r for t, r in zip(temp, RCON[i // 4 - 1])]  # Add RCON
#         words.append([w ^ t for w, t in zip(words[i - 4], temp)])
#
#     return words
#
# def format_key_schedule(words: List[List[int]]):
#     for i in range(0, len(words), 4):
#         round_keys = words[i:i + 4]
#         print(f"Round {i // 4}: " + " ".join("".join(f"{byte:02x}" for byte in word) for word in round_keys))
#
# if __name__ == "__main__":
#     cipher_key_hex = "2b7e151628aed2a6abf7158809cf4f3c"
#     cipher_key = [int(cipher_key_hex[i:i+2], 16) for i in range(0, len(cipher_key_hex), 2)]
#
#     key_schedule = key_expansion(cipher_key)
#
#     format_key_schedule(key_schedule)
