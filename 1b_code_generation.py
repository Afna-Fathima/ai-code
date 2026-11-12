print("URK23CS1273")

def n_nat_numbers(n):
    return list(range(n + 1))

test_cases = [
    (0, [0]),
    (1, [0, 1]),
    (3, [0, 1, 2, 3]),
    (5, [0, 1, 2, 3, 4, 5]),
    (10, list(range(11)))
]

for n, expected in test_cases:
    result = n_nat_numbers(n)
    print("Input:", n, "Output:", result)
    print("PASS" if result == expected else "FAIL")
