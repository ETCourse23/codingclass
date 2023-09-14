def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
num = 5
result = factorial_recursive(num)
print(f"The factorial of {num} is {result}")
