def factorial(n):
    return n if n == 1 else factorial(n - 1) * n
# Driver
print(factorial(5))