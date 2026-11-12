import ast

print("URK23CS1273")

code = """
def add_numbers(a, b):
    return a + b

print(add_numbers(10, 20))
"""

# Syntax checking
try:
    ast.parse(code)
    print("Syntax Check: PASS")
except SyntaxError:
    print("Syntax Check: FAIL")

# Execution checking
try:
    exec(code)
    print("Execution Check: PASS")
except Exception as e:
    print("Execution Check: FAIL", e)

# Test cases
def add_numbers(a, b):
    return a + b

tests = [
    (2, 3, 5),
    (10, 20, 30),
    (-2, 2, 0),
    (0, 0, 0)
]

passed = 0
for a, b, expected in tests:
    if add_numbers(a, b) == expected:
        passed += 1

print("Tests Passed:", passed, "/", len(tests))
score = (passed / len(tests)) * 100
print("Quality Score:", score, "%")

if score == 100:
    print("Code Quality: GOOD")
else:
    print("Code Quality: NEEDS IMPROVEMENT")
