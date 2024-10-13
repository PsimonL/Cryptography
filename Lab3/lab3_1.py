def generate_stream_a(initial_vector):
    z = list(initial_vector)
    stream = z[:]

    for _ in range(100):
        new_bit = (z[0] + z[1] + z[2] + z[3]) % 2
        z.append(new_bit)
        stream.append(new_bit)
        z.pop(0)

    return stream


def generate_stream_b(initial_vector):
    z = list(initial_vector)
    stream = z[:]

    for _ in range(100):
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


def format_stream(stream):
    return ''.join(map(str, stream[:50]))


test_vector_a = [0, 1, 0, 0]
test_vector_b = [1, 0, 0, 0]

test_stream_a = generate_stream_a(test_vector_a)
test_stream_b = generate_stream_b(test_vector_b)

print("Dane testowe:")
print(f"a - wektor: {''.join(map(str, test_vector_a))}")
print(f"a - strumien: {format_stream(test_stream_a)}")
print(f"b - wektor: {''.join(map(str, test_vector_b))}")
print(f"b - strumien: {format_stream(test_stream_b)}")

initial_vectors = [(a, b, c, d) for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1)]

print("\nWyniki a:")
for vector in initial_vectors:
    stream = generate_stream_a(vector)
    period = find_period(stream)
    print(f"P({''.join(map(str, vector))})={period}")

print("\nWyniki b:")
for vector in initial_vectors:
    stream = generate_stream_b(vector)
    period = find_period(stream)
    print(f"P({''.join(map(str, vector))})={period}")
