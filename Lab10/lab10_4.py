from hashlib import md5


def calculate_md5(data):
    """Oblicza hash MD5 dla podanych danych."""
    return md5(data).hexdigest()


def find_differences(data1, data2):
    """Porównuje dwie wiadomości i znajduje różnice między nimi."""
    diff_positions = []
    for i, (b1, b2) in enumerate(zip(data1, data2)):
        if b1 != b2:
            diff_positions.append(i)
    return diff_positions


def display_differences(data1, data2):
    """Wyświetla różnice między dwiema wiadomościami w formie czytelnej."""
    diff_positions = find_differences(data1, data2)
    for pos in diff_positions:
        print(f"Position {pos}: {data1[pos]:02x} != {data2[pos]:02x}")


def bytes_from_hex_string(hex_string):
    """Konwertuje ciąg hex na bajty."""
    return bytes.fromhex(hex_string.replace(" ", "").replace("\n", ""))


def hash_and_compare_messages(messages):
    """Oblicza MD5 dla wiadomości i porównuje w parach."""
    hashes = {}
    for name, data in messages.items():
        hashes[name] = calculate_md5(data)
        print(f"Message {name} hash: {hashes[name]}")

    print("\nComparing pairs:")
    pairs = [("M1", "M2"), ("M1", "M3"), ("M2", "M3")]

    for m1, m2 in pairs:
        print(f"Comparing {m1} and {m2}:")
        if hashes[m1] == hashes[m2]:
            print(f"  Collision detected between {m1} and {m2}!")
            display_differences(messages[m1], messages[m2])
        else:
            print(f"  No collision.")


if __name__ == "__main__":
    messages = {
        "M1": bytes_from_hex_string("""
            d1 31 dd 02 c5 e6 ee c4 69 3d 9a 06 98 af f9 5c
            2f ca b5 87 12 46 7e ab 40 04 58 3e b8 fb 7f 89
            55 ad 34 06 09 f4 b3 02 83 e4 88 83 25 71 41 5a
            08 51 25 e8 f7 cd c9 9f d9 1d bd f2 80 37 3c 5b
            d8 82 3e 31 56 34 8f 5b ae 6d ac d4 36 c9 19 c6
            dd 53 e2 b4 87 da 03 fd 02 39 63 06 d2 48 cd a0
            e9 9f 33 42 0f 57 7e e8 ce 54 b6 70 80 a8 0d 1e
            c6 98 21 bc b6 a8 83 93 96 f9 65 2b 6f f7 2a 70
        """),
        "M2": bytes_from_hex_string("""
            d1 31 dd 02 c5 e6 ee c4 69 3d 9a 06 98 af f9 5c
            2f ca b5 07 12 46 7e ab 40 04 58 3e b8 fb 7f 89
            55 ad 34 06 09 f4 b3 02 83 e4 88 83 25 f1 41 5a
            08 51 25 e8 f7 cd c9 9f d9 1d bd 72 80 37 3c 5b
            d8 82 3e 31 56 34 8f 5b ae 6d ac d4 36 c9 19 c6
            dd 53 e2 34 87 da 03 fd 02 39 63 06 d2 48 cd a0
            e9 9f 33 42 0f 57 7e e8 ce 54 b6 70 80 28 0d 1e
            c6 98 21 bc b6 a8 83 93 96 f9 65 ab 6f f7 2a 70
        """),
        "M3": bytes_from_hex_string("""
            d1 31 dd 02 c5 e6 ee c4 69 3d 9a 06 98 af f9 5c
            2f ca b5 07 12 46 7e ab 40 04 58 3e b8 fb 7f 89
            55 ad 34 06 09 f4 b3 02 83 e4 88 83 25 f1 41 5a
            08 51 25 e8 f7 cd c9 9f d9 1d bd 72 80 37 3c 5b
            d8 82 3e 31 56 34 8f 5b ae 6d ac d4 36 c9 19 c6
            dd 53 e2 34 87 da 03 fd 02 39 63 06 d2 48 cd a0
            e9 9f 33 42 0f 57 7e e8 ce 54 b6 70 80 28 0d 1e
            c6 98 31 bc b6 a8 83 93 96 f9 65 ab 6f f7 2a 70
        """),
    }

    hash_and_compare_messages(messages)
