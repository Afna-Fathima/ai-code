print("URK23CS1273")

def complete_code(code):
    if "factorial" in code:
        return code + """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
"""
    elif "reverse" in code:
        return code + """
    return text[::-1]
"""
    else:
        return code + "\n    return None"

code1 = "def factorial(n):"
code2 = "def reverse(text):"

print("Completed Code 1:")
print(complete_code(code1))

print("Completed Code 2:")
print(complete_code(code2))
