import math

def discriminant(a, b, c):
    D = b**2 - 4*a*c

    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a

    return f"L = {x1, x2}"

def main():
    print(discriminant(1, 7, -8)) # 1 -8

main()
