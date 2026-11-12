print("URK23CS1273")

real_code = [
    "def add(a,b): return a+b",
    "def square(n): return n*n",
    "def factorial(n): return 1 if n==0 else n*factorial(n-1)"
]

generated_code = "def sort_list(arr): return sorted(arr)"

print("Generated Code:")
print(generated_code)

print("\nDiscriminator Results:")
for code in real_code:
    print("REAL:", code)

print("\nGENERATED:", generated_code)
print("Code Generation Completed")
