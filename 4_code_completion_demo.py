print("URK23CS1273")

def code_completion(code):
    if not code.strip():
        return "Enter some Python code."

    completion = """
    total = sum(numbers)
    average = total / len(numbers)
    return average
    """
    return code + completion

prompt = "def calculate_average(numbers):"
print("Input Code:")
print(prompt)

print("\nCompleted Code:")
print(code_completion(prompt))
