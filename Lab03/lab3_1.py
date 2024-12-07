def generate_stream(initial_vector, mode='a'):
    z = list(initial_vector)
    stream = z[:]

    for _ in range(100):
        if mode == 'a':
            new_bit = (z[0] + z[1] + z[2] + z[3]) % 2
        elif mode == 'b':
            new_bit = (z[0] + z[3]) % 2
            
        z.append(new_bit)
        stream.append(new_bit)
        z.pop(0)

    return stream


def find_period(stream):
    n = len(stream)
    
    for period_length in range(1, n // 2 + 1):
        if stream[:period_length] == stream[period_length:2 * period_length]:
            if all(stream[i] == stream[i + period_length] for i in range(n - period_length)):
                return period_length
    return n


test_vector_a = [0, 1, 0, 0]
test_vector_b = [1, 0, 0, 0]

test_stream_a = generate_stream(test_vector_a, mode='a')
test_stream_b = generate_stream(test_vector_b, mode='b')

print("Dane testowe:")
print(f"a - wektor: {''.join(map(str, test_vector_a))}")
print(f"a - strumien klucza: {''.join(map(str, test_stream_a[:50]))}")
print(f"b - wektor: {''.join(map(str, test_vector_b))}")
print(f"b - strumien klucza: {''.join(map(str, test_stream_b[:50]))}")

all_possible_vectors = [(a, b, c, d) for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1)]

print("\nWyniki - a:")
for vector in all_possible_vectors:
    stream = generate_stream(vector, mode='a')
    period = find_period(stream)
    print(f"P({''.join(map(str, vector))})={period}")

print("\nWyniki - b:")
for vector in all_possible_vectors:
    stream = generate_stream(vector, mode='b')
    period = find_period(stream)
    print(f"P({''.join(map(str, vector))})={period}")
